import sys
import random
from pyfiglet import Figlet

list_fonts = Figlet().getFonts()

if len(sys.argv) == 1:
    f = random.choice(list_fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Incorrect usage")

    f = sys.argv[2]
    if f not in list_fonts:
        sys.exit("Invalid font")
        
else:
    sys.exit("Incorrect usage")

input = input("Input: ")

output = Figlet(font=f)
print("Output:")
print(output.renderText(input))