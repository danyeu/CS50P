import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if valid := re.search(r"(?:[a-z0-9])+", s, re.IGNORECASE):
        return True
    return False


if __name__ == "__main__":
    main()