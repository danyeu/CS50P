import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if valid := re.search(r"^(?:(?:2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])\.){3}(?:2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])$", ip):
        return True
    return False


if __name__ == "__main__":
    main()
