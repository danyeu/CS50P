import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a csv file")

try:
    f = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

reader = csv.reader(f)

menu = []
for row in reader:
    menu_item = []
    for col in row:
        menu_item.append(col)
    menu.append(menu_item)

print(tabulate(menu, headers="firstrow", tablefmt="grid"))

f.close