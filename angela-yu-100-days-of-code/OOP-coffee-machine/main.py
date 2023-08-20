from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = input(f"What would you like? ({Menu().get_items()})\n")

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while choice is not "off":
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    choice = input(f"What would you like? ({Menu().get_items()})\n")
