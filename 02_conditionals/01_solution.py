age = int(input("Proved me your age: "))

if age <= 0:
    print("ERROR, age can not be 0 or less than 0")
    exit()

if age < 13:
    print("You are a Child")

elif age < 20:
    print("You are a Teenager")
    
elif age <60:
    print("You are an Adult")

else: 
    print("You are a Senior")
