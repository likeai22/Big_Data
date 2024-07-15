import sys

total_count = 0
variance_sum = 0.0
mean = None

for line in sys.stdin:
    price, mean_str = line.strip().split("\t")
    try:
        price = float(price)
        mean = float(mean_str)
        variance_sum += (price - mean) ** 2
        total_count += 1
    except ValueError:
        continue

if total_count > 0 and mean is not None:
    variance = variance_sum / total_count
    print(f"{variance}")
