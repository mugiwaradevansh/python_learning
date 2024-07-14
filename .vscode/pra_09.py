fruits = str(input("Enter the fruit name:"))
ripness = str(input("Enter the fruit color:"))

if ripness == "green":
    print(f"{fruits} : is not ripe")
elif ripness == "yellow":
    print(f"{fruits}: is ripe")
elif ripness == "light brown":
    print(f"{fruits}: is medium ripe")
elif ripness == "brown":
    print(f"{fruits}: is unripe")
else:
    print("Invalid input for ripness. Please enter a valid color.")
    