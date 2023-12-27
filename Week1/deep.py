# input into a string

inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()


# only "42" output yes, else output no

if inp == "forty two" or inp == "forty-two" or inp == "42":
    print("Yes")
else:
    print("No")
