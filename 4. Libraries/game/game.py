import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue

    if level > 0:
        break

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess <= 0:
        continue
    
    if guess > answer:
        print("Too large!")
    elif guess < answer:
        print("Too small!")
    else:
        print("Just right!")
        break