import sys
import random
import csv

if len(sys.argv) != 3:
    print("Usage: python random_price_generator_by_csv.py <file name>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    rows = []
    for row in reader:
        name = ['Name']
        price = random.randint(1, 100)
        row['Price'] = price
        rows.append(row)



with open(output_filename, mode='w', newline='') as file:
    fieldnames = ['Name', 'Price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        writer.writerow(row)

print(f"Results saved to {output_filename}")