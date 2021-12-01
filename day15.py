# The coffee machine project

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
        "cost": 3,
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "revenue": 0,
}


def first_display():
    print("Hi. Welcome to the coffee machine!")
    print("Here are your options: ")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Get Resource Status")
    print("5. Exit")


def prepare_report():
    print("Status Report: ")

    for item in resources:
        if item != 'revenue':
            print(f"{item}: {resources[item]}ml")
        else:
            print(f"{item}: ${resources[item]}")

    print()


def check_resources(beverage):
    if beverage == 'espresso':
        water_level = MENU[beverage]['ingredients']['water']
        coffee_level = MENU[beverage]['ingredients']['coffee']
        if resources['water'] < water_level or resources['coffee'] < coffee_level:
            return False
        else:
            return True
    else:
        water_level = MENU[beverage]['ingredients']['water']
        milk_level = MENU[beverage]['ingredients']['milk']
        coffee_level = MENU[beverage]['ingredients']['coffee']
        if resources['water'] < water_level or resources['milk'] < milk_level or resources['coffee'] < coffee_level:
            return False
        else:
            return True


def update_resources(drink):
    for item in drink:
        resources[item] = resources[item] - drink[item]


def prepare_espresso():
    if check_resources('espresso'):
        update_resources(MENU['espresso']['ingredients'])
        resources['revenue'] += MENU['espresso']['cost']
        print("Your espresso is ready. Enjoy!")
        print()
    else:
        print("Sorry this drink is unavailable right now")
        print()


def prepare_latte():
    if check_resources('latte'):
        update_resources(MENU['latte']['ingredients'])
        resources['revenue'] += MENU['latte']['cost']
        print("Your latte is ready. Enjoy!")
        print()
    else:
        print("Sorry this drink is unavailable right now")
        print()


def prepare_cappuccino():
    if check_resources('cappuccino'):
        update_resources(MENU['cappuccino']['ingredients'])
        resources['revenue'] += MENU['cappuccino']['cost']
        print("Your cappuccino is ready. Enjoy!")
        print()
    else:
        print("Sorry this drink is unavailable right now")
        print()


machine_on = True
while machine_on:
    first_display()
    option = int(input('Please enter the option!\n'))
    if 0 <= option < 5:
        if option == 0:
            print("Bye! See you soon!")
            machine_on = False
        elif option == 1:
            prepare_espresso()
        elif option == 2:
            prepare_latte()
        elif option == 3:
            prepare_cappuccino()
        elif option == 4:
            prepare_report()
    else:
        print("invalid choice. try again")
