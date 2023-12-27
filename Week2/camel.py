# store input into a string

inp = input("camelCase: ")


# print each letter in the string

for c in inp:
    # condition if an uppercase letter is in the string
    if c.isupper():
        print("_" + c.lower(), end = "")
    else:
        print(c, end = "")


# new line

print("\n")
