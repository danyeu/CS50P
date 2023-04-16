from datetime import date
import inflect
import sys


def main():
    dob = input("Date of Birth (YYYY-MM-DD): ").strip()
    try:
        date.fromisoformat(dob)
    except ValueError:
        sys.exit("invalid date")

    minutes = minutes_alive(dob)
    minutes_word = minutes_to_words(minutes)

    print(minutes_word)


def minutes_alive(date_string):
    date_obj = date.fromisoformat(date_string)
    today = date.today()
    if date_obj > today:
        sys.exit("invalid date")
    delta = divmod((today - date_obj).total_seconds(), 60)[0]
    return int(round(delta, 0))


def minutes_to_words(minutes: int):
    p = inflect.engine()
    return p.number_to_words(minutes).replace(" and ", " ").capitalize() + " minutes"


if __name__ == "__main__":
    main()