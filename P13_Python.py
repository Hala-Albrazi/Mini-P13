items = []
prices = []
print("..Welcome to Ishop calculator..")
many = int(input("How many items do you have in your basket?  "))
if many > 0:
    print("Let's go to count them...")
    for i in range(0, many):
        item = (input(f"Please tell me the name of item number {i+1}.. "))
        items.append(item)
        price = float(input(f"What is the price of {item}$?\n"))
        prices.append(price)
else:
    print("So you are not in mood for shopping!!")
Q = input("Would you like to see the basket?\n")
if Q == "yes":
    print(items)
else:
    print("As you like!")
cost = input("Would you like to see how much it costs?  ")
if cost == "yes":
    print(f"The total cost will be: {sum(prices)} $")
else:
    print("okay!!!!!!")
