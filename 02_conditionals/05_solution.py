weather_input = input("Please the enter the weather: ")
weather = weather_input.lower()

if weather == "sunny":
    activity = "Go for a walk"

elif weather == "rainy":
    activity = "Read a book"
    
elif weather == "snowy":
    activity = "Build a snowman"
    
print("The suggested activity according to the weather is:", activity)