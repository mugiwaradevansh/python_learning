colors = ["red","white","blue","green","purple"]
for i in colors:
    print(i)
    if i == "green":
        print("\n")
    print("  /next color")
    print(" /end of loop")
    print("/after break")

name = "Devansh"
for lp in name:
    print(lp)
    if lp == "v":
        print(f"{lp} - It's my fav letter")
        continue

for k in range(5):
    print(k)
    if k == 4:
        print("I'm skipping 4")

for i in range(1,11):
    if i%2==1:
        print(i)

py = [i for i in range(1, 58)]
for i in py:
    print(i)
    if i == 45:
        print(i * [3] + 300)
