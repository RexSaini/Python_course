order_size = input("Please enter your order size: ")

input_shot = input("Do you want extra espresso shot y/n: ")
extra_shot = input_shot.lower()

if extra_shot == "y":
    coffee = order_size + " coffee with extra shot of espresso"

elif extra_shot == "n":
    coffee = order_size + " coffee without extra shot of espresso"

print("Your order is:", coffee)