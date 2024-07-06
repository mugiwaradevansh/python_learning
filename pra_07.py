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