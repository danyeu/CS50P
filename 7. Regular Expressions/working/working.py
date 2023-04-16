import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if valid := re.search(r"^(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)$", s):
        groups = [None] * 7
        for i in range(1,7):
            groups[i] = valid.group(i)

        if valid.group(3) == "PM":
            if valid.group(1) != "12":
                groups[1] = str(int(valid.group(1)) + 12)
        elif valid.group(1) == "12":
            groups[1] = "00"

        if valid.group(6) == "PM":
            if valid.group(4) != "12":
                groups[4] = str(int(valid.group(4)) + 12)
        elif valid.group(4) == "12":
            groups[4] = "00"

        output=""

        output += f"{int(groups[1]):02d}"

        if not groups[2]:
            groups[2] = ":00"
        output+=groups[2]

        output += " to "

        output += f"{int(groups[4]):02d}"

        if not groups[5]:
            groups[5] = ":00"
        output += groups[5]

        return output

    raise ValueError("Invalid format")


if __name__ == "__main__":
    main()