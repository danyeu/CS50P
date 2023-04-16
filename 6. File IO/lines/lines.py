import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-3:] != ".py":
    sys.exit("Not a python file")

try:
    f = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

lines = 0

for line in f:
    line = line.strip("\n").strip()
    if not line:
        continue
    if line[0] == "#":
        continue
    lines += 1

print(lines)

f.close