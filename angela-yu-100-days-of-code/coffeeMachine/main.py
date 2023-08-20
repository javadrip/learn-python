MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

report = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
    "revenue": 0
}

is_on = True


def check_resources(drink):
    ingredients = MENU[drink].get("ingredients", {})

    water_required = ingredients.get("water", 0)
    milk_required = ingredients.get("milk", 0)
    coffee_required = ingredients.get("coffee", 0)

    if resources['water'] < water_required:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < milk_required:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < coffee_required:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def insert_coins():
    coin = input("Insert quarters, dimes, nickles or pennies: ")
    return coin


def check_coins(balance, cost):
    coin = insert_coins()

    if coin == "q":
        balance += 0.25
    elif coin == "d":
        balance += 0.1
    elif coin == "n":
        balance += 0.05
    elif coin == "p":
        balance += 0.01
    else:
        balance += 0

    if balance < cost:
        print(f"Remaining: {cost - balance}")
        check_coins(balance, cost)
    elif balance >= cost:
        print(f"Change: {balance - cost}")


def make_coffee(drink, cost):
    ingredients = MENU[drink].get("ingredients", {})

    water_used = ingredients.get("water", 0)
    milk_used = ingredients.get("milk", 0)
    coffee_used = ingredients.get("coffee", 0)

    resources["water"] -= water_used
    report["water"] += water_used

    resources["milk"] -= milk_used
    report["milk"] += milk_used

    resources["coffee"] -= coffee_used
    report["coffee"] += coffee_used

    report["revenue"] += cost


while is_on:
    drink = input("What would you like? \n   1. Espresso\n   2. Latte\n   3. Cappuccino\n").lower()

    if drink == "off":
        print("Maintenance")
        is_on = False
    elif drink == "report":
        print(f"Water: {report['water']}ml")
        print(f"Milk: {report['milk']}ml")
        print(f"Coffee: {report['coffee']}g")
        print(f"Revenue: ${report['revenue']}")
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        cost = MENU[drink]['cost']
        print(f"The drink costs ${cost}0")

        balance = 0

        if check_resources(drink) is False:
            print(f"We can't make your {drink}")
        else:
            check_coins(balance, cost)
            print(f"Making your {drink}")
            make_coffee(drink, cost)

        print(f"Here is your {drink}. Enjoy!")
