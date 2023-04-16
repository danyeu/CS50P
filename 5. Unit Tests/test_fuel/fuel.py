def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            print(gauge(convert(fraction)))
            break
        except:
            continue


# expects X / Y
def convert(fraction):
    numbers = fraction.split("/")

    # raises ValueError if not int
    numbers = [int(x) for x in numbers]

     # raise ZeroDivisionError if Y == 0
    if numbers[1] == 0:
        raise ZeroDivisionError

    # raise ValueError if X > Y
    if numbers[0] > numbers[1]:
        raise ValueError

    return int(round((numbers[0] / numbers[1]) * 100, 0))


# expects int
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()