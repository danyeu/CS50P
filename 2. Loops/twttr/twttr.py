input = input("Input: ")
output = ""
vowels = ["A", "E", "I", "O", "U"]

for char in input:
    if char.upper() not in vowels:
        output += char

print(f"Output: {output}")
