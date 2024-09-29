with open("latency_base.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a float and calculate the mean
latency_values = [float(line.strip()) for line in lines if line.strip()]
mean_latency = sum(latency_values) / len(latency_values) if latency_values else 0
len_base = len(latency_values)

print(f"Mean Latency: {mean_latency} ms")
# Mean Latency: 1.2136425190514741 ms


with open("latency_io.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a float and calculate the mean
latency_values = [float(line.strip()) for line in lines if line.strip()]
mean_latency = sum(latency_values[:len_base]) / len(latency_values[:len_base]) if latency_values else 0

print(f"Mean Latency Optimized: {mean_latency} ms")
# Mean Latency: 1.2136425190514741 ms