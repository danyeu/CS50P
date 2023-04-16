while True:
    fraction = input("Fraction: ").strip()

    numbers = fraction.split("/")
    if len(numbers) != 2:
        continue

    try:
        numbers = [int(x) for x in numbers]
    except ValueError:
        continue

    if numbers[1] == 0:
        continue

    percentage = numbers[0] / numbers[1]
    if not 0 <= percentage <= 1:
        continue

    break


if percentage <= 0.01:
    print("E")
elif percentage >= 0.99:
    print("F")
else:
    print(f"{percentage * 100:.0f}%")

