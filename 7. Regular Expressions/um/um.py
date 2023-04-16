import re


def main():
    print(count(input("Text: ")))


def count(s):
    valid = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(valid)


if __name__ == "__main__":
    main()