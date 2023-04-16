months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


while True:
    user_date = input("Date: ").strip().title()

    if len(user_date.split("/")) == 3:
        user_date_list = user_date.split("/")

        try:
            user_date_list = list(map(int, user_date_list))
        except ValueError:
            continue

    elif len(user_date.split(" ")) == 3:
        user_date_list = user_date.split(" ")

        try:
            if user_date_list[1][-1] != ",":
                continue
        except IndexError:
            continue

        user_date_list[1] = user_date_list[1][:-1]

        if user_date_list[0] not in list(months):
            continue
        else:
            user_date_list[0] = months[user_date_list[0]]

        try:
            user_date_list[1] = int(user_date_list[1])
            user_date_list[2] = int(user_date_list[2])
        except ValueError:
            continue

    else:
        continue

    if not 1 <= user_date_list[0] <= 12:
        continue

    if not 1 <= user_date_list[1] <= 31:
        continue

    if not 0 <= user_date_list[2]:
        continue

    output = f"{user_date_list[2]:04}-{user_date_list[0]:02}-{user_date_list[1]:02}"
    break

print(output)