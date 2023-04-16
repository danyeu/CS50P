import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if valid := re.search(r"src *= *\" *(?:https?://(?:www.)?)?youtube.com/embed/([a-z0-9]+)", s, re.IGNORECASE):
        return "https://youtu.be/" + valid.group(1)
    return None


if __name__ == "__main__":
    main()