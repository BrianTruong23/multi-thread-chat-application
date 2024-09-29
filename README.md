# Async IO Socket Server
## Introduction
- This project is a simple socket server implemented in Python. It handles multiple client connections concurrently using asynchronous I/O (async IO) and a thread pool. The server can broadcast messages to all connected clients and measure the latency of message handling.

## Background
- Traditional synchronous socket servers can become inefficient when handling multiple client connections, as each connection may block the server while waiting for I/O operations to complete. This can lead to increased latency and potential message loss, especially under high load.

To address these issues, this project leverages async IO to handle multiple client connections concurrently without blocking. By using async IO, the server can efficiently manage I/O-bound operations, improving performance and reducing message loss.
## What I Did
- Implemented a Socket Server: Created a basic socket server that listens for incoming client connections and handles them using a thread pool.
- Client Handling: Developed a function to manage client connections, receive messages, and broadcast them to other clients.
- Latency Measurement: Added functionality to measure and log the latency of message handling.
- HTTP Response: Implemented a simple HTTP response to acknowledge client messages.

## Improvements with Async IO
- Non-blocking Operations: Replaced blocking I/O operations with non-blocking async IO, allowing the server to handle multiple connections concurrently without waiting for I/O operations to complete.
- Efficient Resource Utilization: Utilized an event loop to manage I/O operations efficiently, reducing resource consumption and improving scalability.
- Reduced Message Loss: By handling multiple connections concurrently and efficiently, the server is less likely to experience message loss due to delays or blocking.
- Simplified Concurrency: Used async IO to achieve concurrency without the complexity and overhead of threading, making the server more robust and easier to maintain.
