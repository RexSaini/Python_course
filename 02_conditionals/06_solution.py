distance = float(input("Enter the distance in km: "))

if distance <= 0:
    print("ERROR, the distance can not be 0 or less than 0 km")
    exit()

if distance < 3:
    transportation_mode = "Walk"

elif distance <= 15:
    transportation_mode = "Bike"

else:
    transportation_mode = "Car"

print("The recommended transportation mode is", transportation_mode)