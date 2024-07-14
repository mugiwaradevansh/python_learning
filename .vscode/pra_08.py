grade = int(input("enter the number of the marks :"))

if grade >=101:
    print("invalid input ")
    exit()

if grade >= 90:
    print(f"{grade} :is A")

elif grade >= 80:
    print(f"{grade} :is B")

elif grade >= 70 :
    print(f"{grade} :is C")

elif grade >= 60 :
    print(f"{grade} : is D")

else:
    print(f"{grade} : is cont in failed")