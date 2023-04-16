# Assumes "A ? B", where ? in [+, -, *, /] and B != 0 when ? = /
equation = input("Enter equation: ")
print(f"{eval(equation):.1f}")