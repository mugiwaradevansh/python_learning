age = int(input("enter your age :" ))
print("\n")

day = input("enter the day:")
print("\n")

if age>=18:
    price =12
else :
    price = 10
if day == "wednesday":
    price -=2

print (f"your ticket price ---{price}--- after the all T&M")