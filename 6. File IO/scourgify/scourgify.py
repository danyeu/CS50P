import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
    sys.exit("Both files must be in csv format")

try:
    f1 = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

reader = csv.DictReader(f1)

after = []
for row in reader:
    after.append({"first": row["name"].split(", ")[1], "last": row["name"].split(", ")[0], "house": row["house"]})

f1.close

try:
    f2 = open(sys.argv[2], "w")
except Exception:
    sys.exit(f"Could not write to {sys.argv[2]}")

writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
writer.writeheader()
for row in after:
    writer.writerow(row)

f2.close
