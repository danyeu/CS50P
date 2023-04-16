import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].split(".")[-1].lower() not in ["jpg", "jpeg", "png"]:
    sys.exit(f"{sys.argv[1]} not a png or jpeg file")

if sys.argv[2].split(".")[-1].lower() != sys.argv[1].split(".")[-1].lower():
    sys.exit("Input and output have different extensions")

try:
    before = Image.open(sys.argv[1])
except Exception:
    sys.exit(f"Could not open {sys.argv[1]}")

try:
    shirt = Image.open("shirt.png")
except Exception:
    sys.exit(f"Could not open shirt.png")

size = shirt.size

before = ImageOps.fit(before, size)

before.paste(shirt, shirt)

try:
    before.save(sys.argv[2])
except Exception:
    sys.exit(f"Could not save {sys.argv[2]}")