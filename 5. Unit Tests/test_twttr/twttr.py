def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    vowels = ["A", "E", "I", "O", "U"]
    output = ""
    for char in word:
        if char.upper() not in vowels:
            output += char
    return output


if __name__ == "__main__":
    main()