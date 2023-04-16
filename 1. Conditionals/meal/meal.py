def main():
    current_time = convert(input("Current time: "))
    if 7 <= current_time <= 8:
        print("breakfast time")
    elif 12 <= current_time <= 13:
        print("lunch time")
    elif 18 <= current_time <= 19:
        print("dinner time")


def convert(time):
    time = list(map(float, time.split(":")))
    return time[0] + time[1] / 60


if __name__ == "__main__":
    main()