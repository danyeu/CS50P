price = 50
coins = [25, 10, 5]

paid = 0
while paid < price:
    print(f"Amount Due: {price - paid}")
    coin = input("Insert Coin: ")
    try:
        coin = int(coin)
    except ValueError:
        continue

    if coin not in coins:
        continue

    paid += coin

print(f"Change Owed: {paid - price}")
