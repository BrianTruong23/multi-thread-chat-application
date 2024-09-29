import asyncio
import json
import time

clients = []

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"New connection: {addr}")
    clients.append(writer)
    try:
        while True:
            start_time = time.time()  # Start time for latency measurement
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"{addr}: {message}")
            await broadcast(message, writer)
            # Send a proper HTTP response back to the client
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/json\r\n"
                "Content-Length: 17\r\n"
                "\r\n"
                '{"status": "ok"}'
            )
            writer.write(response.encode('utf-8'))
            await writer.drain()
            end_time = time.time()  # End time for latency measurement
            latency = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"Latency for {addr}: {latency} ms")
            # Append latency value with a newline
            with open('../latency_script/latency_io.txt', "a") as f:
                f.write(f"{latency}\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"Connection closed: {addr}")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

async def broadcast(message, writer):
    for client in clients:
        if client != writer:
            try:
                client.write(message.encode('utf-8'))
                await client.drain()
            except Exception as e:
                print(f"Error broadcasting to client: {e}")
                clients.remove(client)

async def start_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 12345)
    addr = server.sockets[0].getsockname()
    print(f"Server started on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())
