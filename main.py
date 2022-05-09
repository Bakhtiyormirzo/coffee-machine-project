

RESOURCE = {
    "water" : 800,
    "milk" : 400,
    "coffee" : 150,
    "money" : 0
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

PRICE = {
    "espresso" : 2.5,
    "latte" : 2.75,
    "cappuccino" : 4.5
}

running = True
while running:
    coffee = input("What would you like (espresso/latte/cappuccino)? ")

    if coffee == "off":
        running = False
        continue

    if coffee == "report":
        for k, v in RESOURCE.items():
            if k == "water" or k == "milk":
                print(f"{k} : {v}ml")
            elif k == "coffee":
                print(f"{k} : {v}g")
            else:
                print(f"{k} : ${v}")

        pass # print report here --> whatever is left (water/milk/coffee/money)

    else:
        pass


