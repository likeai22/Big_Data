import sys
import csv

input = csv.reader(sys.stdin)
next(input)

prices = []
total_sum = 0.0
total_count = 0

for fields in input:
    if len(fields) > 9:
        try:
            price = float(fields[9])
            prices.append(price)
            total_sum += price
            total_count += 1
        except ValueError:
            continue

if total_count > 0:
    mean = total_sum / total_count
    for price in prices:
        print(f"{price}\t{mean}")
