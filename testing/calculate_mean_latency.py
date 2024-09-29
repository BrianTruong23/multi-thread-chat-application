with open("../latency_script/latency_base.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a float and calculate the mean
latency_values_base = [float(line.strip()) for line in lines if line.strip()]
mean_latency_base = sum(latency_values_base) / len(latency_values_base) if latency_values_base else 0
len_base = len(latency_values_base)

print(f"Mean Latency: {mean_latency_base} ms")


with open("../latency_script/latency_thread.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a float and calculate the mean
latency_values_io = [float(line.strip()) for line in lines if line.strip()]
mean_latency_optimized = sum(latency_values_io[:len_base]) / len(latency_values_io[:len_base]) if latency_values_io else 0

print(f"Mean Latency Optimized: {mean_latency_optimized} ms")

with open('latency_report.txt', "w") as f:
    f.write(f"Mean Latency: {mean_latency_base} ms \n")
    f.write(f"Mean Latency Optimized: {mean_latency_optimized} ms")