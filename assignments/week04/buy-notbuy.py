prices = []
total_buy = 0
bought = []
print("Enter prices of 6  items: ")
for i in range(1, 7):
    item = int(input(f"Item {i}:"))
    prices.append(item)

print()
budget = int(input("Enter total budget: " ))
print()
for i in range(len(prices)):
    if total_buy + prices[i] <= budget:
        print (f"Item {i+1} = {prices[i]} -> buy")
        total_buy += prices[i]
        bought.append(prices[i])
        print(f"Current total = {total_buy}")
    else:
        print (f"Item {i+1} = {prices[i]} -> cannot buy")
        print(f"Current total = {total_buy}")
    print()

print(f"Bought items: {bought}" )
print(f"Total spent: {total_buy}")
print(f"Remaining budget: {budget - total_buy}")