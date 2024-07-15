import sys
import csv

input = csv.reader(sys.stdin)
next(input)

for fields in input:
    if len(fields) > 9:
        try:
            price = float(fields[9])
            print(f"{price}\t1")
        except ValueError:
            continue
