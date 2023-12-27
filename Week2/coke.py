# initial amount

cost = 50
print("Amount Due:", cost)


# coin input & print conditions

while True:
    coin_in = int(input("Insert Coin: ").strip())

    # only 25, 10, 5 cents
    if coin_in == 25 or coin_in == 10 or coin_in == 5:
        cost -= coin_in

        if cost > 0:
            print("Amount Due:", cost)
        else:
            print("Change Owed:", -cost)
            break

    # otherwise return the cost
    else:
        print("Amount Due:", cost)
