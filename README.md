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


## Result 
For testing the result with async io, I utilized locust library to measure the concurrency, request failures and reponse time of both servers. For more detailed reports, the files are located under report folders. 

With the baseline server, there is significant message loss. Out of 11,717 requests, 3,197 requests fail, resulting in a failure rate of 27%. The response time is also relatively higher, indicating potential bottlenecks that reduce overall server efficiency.

![Report of Baseline Server (Number of Requests)]("/image/report_base.png")
![Report of Baseline Server (Number of Response)]("/image/response_time_base.png")


On the other hand, with the optimized server using Async IO, there is a notable improvement. Out of 34,140 requests, only 6,119 requests fail, reducing the failure rate to 18%. This marks a substantial decrease in failure percentage, showing that the optimized server is capable of handling higher loads with fewer dropped requests. Additionally, the optimized server shows lower response times across different percentiles, which translates to a smoother and more efficient user experience. The increased requests per second and reduced latency indicate that the optimization effectively mitigated the bottlenecks seen in the baseline server.

![Report of Optimized Server with Async IO (Number of Requests)]("/image/report_io.png")
![Report of Optimized Server with Async IO (Number of Response)]("/image/response_time_io.png")
