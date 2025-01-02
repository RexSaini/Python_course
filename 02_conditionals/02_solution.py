age = int(input("Please enter your age: "))

if age <= 0:
    print("ERROR, age can not be 0 or less than 0")
    exit()

day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2
    # price -=2

print("Your ticket price is: $", price)