password = input("Enter your password: ")
password_length = len(password)

if password_length == 0:
    print("ERROR, password can not be empty")
    exit()

if password_length < 6:
    strength = "Weak"

elif password_length <= 10:
    strength = "Medium"

else:
    strength = "Strong"

print("Your password's strength is", strength)