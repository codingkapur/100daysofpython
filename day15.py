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
}


def first_display():
    print("Hi. Welcome to the coffee machine!")
    print("Here are your options: ")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Get resource Status")
    print("0. Exit")


option = -1
machine_on = True
while machine_on:
    first_display()
    option = int(input('Please enter the option!'))
    if(option>=0 and option<5):
        machine_on= False



# Input screen

def prepare_report():
    print(resources)


def prepare_espresso():
    print(resources)


def prepare_latte():
    print(resources)


def prepare_cappuccino():
    print(resources)


if option == 0:
    print("Bye! See you soon!")
elif option == 1:
    print("Espresso coming up right away!")
    prepare_espresso();
elif option == 2:
    print("Latte coming up right away!")
    prepare_latte();
elif option == 3:
    print("Espresso coming up right away!")
    prepare_cappuccino();
elif option == 5:
    print("Presenting the report right away!")
    prepare_report();
