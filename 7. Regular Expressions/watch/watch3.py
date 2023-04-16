# anything
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if valid := re.search(r".+/embed/([\w^_]+)", s, re.IGNORECASE):
        return "https://youtu.be/" + valid.group(1)
    return None


if __name__ == "__main__":
    main()