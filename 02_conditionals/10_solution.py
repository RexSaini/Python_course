input_pet = str(input("Enter your pet species: ")) 
pet = input_pet.lower()

age = int(input("Enter your pet's age in years: "))

if age <= 0:
    print("ERROR, age can not be 0 or less than 0")
    exit()

if pet == "dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"

elif pet == "cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Kitten food"

print("Food recommended for your", pet, "is", food)