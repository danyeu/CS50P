shopping_list = {}

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        break

    if shopping_list.get(item) is None:
        shopping_list[item] = 1
    else:
        shopping_list[item] += 1

print()

for item in sorted(list(shopping_list)):
    print(f"{shopping_list[item]} {item}")