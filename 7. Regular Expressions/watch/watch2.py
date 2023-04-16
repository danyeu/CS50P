#html only

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if valid := re.search(r"src *= *\" *([^\"]+){1} *\"", s, re.IGNORECASE):
        return valid.group(1)
    return None



if __name__ == "__main__":
    main()