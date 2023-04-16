from validator_collection import validators

try:
    email = validators.email(input("Enter email: "))
    print("Valid")
except ValueError:
    print("Invalid")