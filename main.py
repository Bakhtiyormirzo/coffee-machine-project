RESOURCE = {
    "water" : 800,
    "milk" : 400,
    "coffee" : 50,
    "money" : 10
}

INGREDIENTS = {
    "espresso" : {
        "water" : 200,
        "milk" : 100,
        "coffee" : 10
    },

    "latte" : {
        "water" : 200,
        "milk" : 150,
        "coffee" : 20
    },

    "cappuccino" : {
        "water" : 200,
        "milk" : 120,
        "coffee" : 15
    }
}

MONEY = {
    "quarter" : 0.25,
    "dime" : 0.1,
    "nickle" : 0.05,
    "penny" : 0.01
}

COINS = {
    "quarter" : 10,
    "dime" : 10,
    "nickle" : 10,
    "penny" : 10
}

PRICE = {
    "espresso" : 2.5,
    "latte" : 2.75,
    "cappuccino" : 4.5
}

INGREDIENT_LIST = ["water", "milk", "coffee"]
INPUT_LIST = ["espresso", "latte", "cappuccino", "price", "report", "off", "reset", "coins"]

running = True
while running:
    coffee = input("What would you like (espresso/latte/cappuccino)? ")

    TRANSACTION_SUCCESS = False 

    # checks for spelling issues
    if coffee not in INPUT_LIST:
        continue

    # ending the program
    if coffee == "off":
        running = False
        continue

    # printing report here
    if coffee == "report":
        for k, v in RESOURCE.items():
            if k == "water" or k == "milk":
                print(f"{k} : {v}ml")
            elif k == "coffee":
                print(f"{k} : {v}g")
            else:
                print(f"{k} : ${v}")

        continue

    # printing PRICE here
    if coffee == "price":
        for k, v in PRICE.items():
            print(f"{k} : ${v}")

        continue
    
    # resetting the resources
    if coffee == "reset":
        RESOURCE["water"] = 800
        RESOURCE["milk"] = 400
        RESOURCE["coffee"] = 50

        continue

    # printing the coins
    if coffee == "coins":
        for k, v in COINS.items():
            print(f"{k} : {v}")

        continue

    # taking the order
    else:

        # checking if there is enough water
        if (RESOURCE["water"] - INGREDIENTS[f"{coffee}"]["water"]) < 0:
            print("Sorry, there is not enough water")
            continue
        
        # checking if there is enough milk
        elif (RESOURCE["milk"] - INGREDIENTS[f"{coffee}"]["milk"]) < 0:
            print("Sorry, there is not enough milk")
            continue

        # checking if there is enough coffee
        elif (RESOURCE["coffee"] - INGREDIENTS[f"{coffee}"]["coffee"]) < 0:
            print("Sorry, there is not enough coffee")
            continue

        # runs when there is enough resources to prepare the order
        else:
            print("Insert coins")

        # calculating the total value of inserted coins
        total = 0
        coins = dict()
        for k, v in MONEY.items():
            coins[k] = int(input(f"Insert {v}: "))
            total += v * coins[k]

        # check if enough money is inserted for selected drink
        if total < PRICE[f"{coffee}"]:
            print(f"Sorry that is not enough money. Money refunded.")
            continue

        # offering the change
        elif total > PRICE[f"{coffee}"]:
            
            print("You entered more money. Receive the change.")

            # adding the insterted coins to the number of COINS
            for k in COINS.keys():
                COINS[k] += coins[k] 

            # adding the money to the RESOURCE
            RESOURCE["money"] = round(RESOURCE["money"] + PRICE[f"{coffee}"], 2)

            # amount of change to give back
            change = round(total - PRICE[f"{coffee}"], 2)

            difference = 0
            refunding_coins = {
                "quarter" : 0,
                "dime" : 0,
                "nickle" : 0,
                "penny" : 0
            }

            # used if there is not enough change
            breaking = False

            # calculates how many coins will be given for each coin type
            while difference != change:

                if COINS["quarter"] > 0 and round(difference + 0.25, 2) <= change:
                    difference += 0.25
                    difference = round(difference, 2)
                    refunding_coins["quarter"] += 1

                elif COINS["dime"] > 0 and difference + 0.1 <= change:
                    difference += 0.1
                    difference = round(difference, 2)
                    refunding_coins["dime"] += 1

                elif COINS["nickle"] > 0 and difference + 0.05 <= change:
                    difference += 0.05
                    difference = round(difference, 2)
                    refunding_coins["nickle"] += 1

                elif COINS["penny"] > 0 and difference + 0.01 <= change:
                    difference += 0.01
                    difference = round(difference, 2)
                    refunding_coins["penny"] += 1

                else:
                    print("There is not enough change. Money refunded.")

                    # subtracting the insterted coins to the number of COINS
                    for k in COINS.keys():
                        COINS[k] -= coins[k] 

                     # subtracting the money to the RESOURCE
                    RESOURCE["money"] -= total

                    breaking = True
                    break

            if breaking:
                continue

            # printing the change: number of coins for each type of coin
            print("You are receiving: ")
            for k, v in refunding_coins.items():
                print(f"${MONEY[k]} value of {v} coins")

            TRANSACTION_SUCCESS = True 

        # condition when total money inserted is equal to price, so there is no change needed
        else:
            # adding the insterted coins to the number of COINS
            for k in COINS.keys():
                COINS[k] += coins[k]  

            # adding the money to the RESOURCE
            RESOURCE["money"] += total

            TRANSACTION_SUCCESS = True 
        
        if TRANSACTION_SUCCESS:

            # index for ingredient list (water/milk/coffee)
            i = 0

            for k in RESOURCE.keys():

                # breaks the loop after updating the water/milk/coffee, not money
                if i == 3:
                    break

                RESOURCE[k] -= INGREDIENTS[f"{coffee}"][INGREDIENT_LIST[i]]
                i += 1

        print(f"Here is your {coffee}. Enjoy!")
                

             











