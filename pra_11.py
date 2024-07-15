Number = int(input("Enter number for the table :"))
nums = int(input("Enter the where to you want Table :"))

for i in range(1,nums+1):
    if i == 5:
        continue
    print(f"{Number} x {i} = {i*Number}")

