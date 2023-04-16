import random

MAX_LEVEL = 3

def main():
    level = get_level()

    score = 0
    for _ in range(10):
        lives = 3
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        answer = str(num1 + num2)
        while lives > 0:
            user_answer = input(f"{num1} + {num2} = ").strip()
            if user_answer != answer:
                print("EEE")
                lives -= 1
            else:
                break
        if lives == 0:
            print(f"{num1} + {num2} = {answer}")
        else:
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
        except ValueError:
            continue

        if level in list(range(1, MAX_LEVEL + 1)):
            return level


def generate_integer(level):
    if level not in list(range(1, MAX_LEVEL + 1)):
        raise ValueError

    if level == 1:
        lower = 0
    else:
        lower = 10 ** (level - 1)

    upper = (10 ** level) - 1

    return random.randint(lower, upper)


if __name__ == "__main__":
    main()