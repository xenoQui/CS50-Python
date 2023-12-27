# main function

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# delete "$" & convert to float

def dollars_to_float(d):
    # TODO
    return float(d.replace("$", ""))


# delete % & convert to float

def percent_to_float(p):
    # TODO
    return float(p.replace("%", "")) / 100


main()
