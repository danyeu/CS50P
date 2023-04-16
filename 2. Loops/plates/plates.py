def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2<= len(s) <= 6:
        return False

    # Checks first two chars are alphabetic
    if not s[:2].isalpha():
        return False

    # Checks for non-alphanumeric chars, and if numbers are only at the end
    can_have_numbers = True
    first_number = None
    for char in s[::-1]:
        if not char.isalnum():
            return False
        if char.isdigit():
            if not can_have_numbers:
                return False
            first_number = char
        else:
            can_have_numbers = False

    # Checks if first number is 0
    if first_number == "0":
        return False

    return True


main()