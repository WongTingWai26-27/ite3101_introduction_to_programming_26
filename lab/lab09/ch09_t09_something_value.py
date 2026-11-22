total = 0

for food in prices:
    value = prices[food] * stock[food]
    print(value)
    total += value

print(total)