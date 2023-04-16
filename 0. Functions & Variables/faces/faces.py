def convert(s):
    return s.replace(":)", "🙂").replace(":(","🙁")


def main():
    user_input = input("Enter something: ")
    print(convert(user_input))


main()