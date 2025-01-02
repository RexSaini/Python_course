score = int(input("Enter your score: "))

if score > 100:
    print("ERROR, score can't be more than 100")
    exit()
    
if score < 60:
    print("Your grade is F")

elif score < 70:
    print("Your grade is D")

elif score < 80:
    print("Your grade is C")

elif score < 90:
    print("Your grade is B")

else:
    print("Your grade is A")
