# store an input & split it

inp = input("Expression: ")
x, y, z = inp.split(" ")


# calculate x & z in float, then print

match y:
    case "+":
        num = float(x) + float(z)
    case "-":
        num = float(x) - float(z)
    case "*":
        num = float(x) * float(z)
    case "/":
        num = float(x) / float(z)

print(num)
