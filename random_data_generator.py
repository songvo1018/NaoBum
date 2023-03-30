import sys
import random
import csv
import mimesis

if len(sys.argv) != 3:
    print("Usage: python random_data_generator.py <number>")
    sys.exit(1)

output_filename = sys.argv[2]

try:
    num = int(sys.argv[1])
except ValueError:
    print("Invalid number")
    sys.exit(1)


with open(output_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name'])
    person = mimesis.Person()
    for i in range(num):
        rand_name = person.full_name()
        writer.writerow([rand_name])

print(f"Results saved to {output_filename}")