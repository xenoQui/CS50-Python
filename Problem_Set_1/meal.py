# main function

def main():
    inp = convert(input("What time is it? ").strip())

    if 7 <= inp <= 8:
        print("breakfast time")
    elif 12 <= inp <= 13:
        print("lunch time")
    elif 18 <= inp <= 19:
        print("dinner time")


# convert input to float & return a decimal value

def convert(time):
    hr, min = time.split(":")
    return float(hr) + (float(min) / 60)


# run main function

if __name__ == "__main__":
    main()
