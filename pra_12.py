input_str = input("Enter the string: ")
Reverse_str = ""

for char in input_str:
    Reverse_str = char + Reverse_str

print(Reverse_str)
print(f"The size of Reverse_str is: {len(Reverse_str)}")
print("--------------------------------------------------")

print(char)

print("--------------------------------------------------")
# Print each character with its index in the reversed string
for index, char in enumerate(Reverse_str):
    print(f"Character '{char}' is at index {index}")
