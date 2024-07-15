import sys

total_sum = 0.0
total_count = 0

for line in sys.stdin:
    price, count = line.strip().split("\t")
    try:
        total_sum += float(price)
        total_count += int(count)
    except ValueError:
        continue

if total_count > 0:
    mean = total_sum / total_count
    print(f"{mean}")
