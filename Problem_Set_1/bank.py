# input into a string

inp = input("Greeting: ").strip().lower()


# determine what to print

if inp.startswith("hello"):
    print("$0")
elif inp.startswith("h"):
    print("$20")
else:
    print("$100")
