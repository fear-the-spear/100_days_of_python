# coffee machine (my solution)
from coffee_menu import *


def print_report(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water 💧: {water},\nMilk 🥛: {milk},\nCoffee 🫘: {coffee}")


def use_resources(user_choice):
    for key in resources:
        resources[key] -= MENU[user_choice]["ingredients"][key]


# def check_resources(resources):
#     for key in resources:
#         if resources[key] < MENU[choice]["ingredients"][key]:
#             print(f"Not enough {key}")
        # print(MENU[choice]["ingredients"][key])
    # print(resources)


def inserted_money(quarters, dimes, nickels, pennies):
    total_value_inserted = (quarters + dimes + nickels + pennies)
    return total_value_inserted


print("Welcome to the coffe machine!")


def game():
    machine_running = True
    awaiting_drink = True
    while machine_running:
        while awaiting_drink:
            choice = input(
                "What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "report":
                print_report(resources)

            if choice == 'off':
                print("Thank you, come again!")
                quit()

            if choice != "report" and choice != 'exit':
                # print(MENU[choice])
                for key in resources:
                    if resources[key] < MENU[choice]["ingredients"][key]:
                        print(f"Not enough {key}")
                        game()
                    else:
                        awaiting_drink = False

                accepting_money = True
                while accepting_money:
                    print("Please insert coins.")

                    quarters = int(input("How many quarters?: ")) * .25
                    dimes = int(input("How many dimes?: ")) * .1
                    nickels = int(input("How many nickels?: ")) * .05
                    pennies = int(input("How many pennies?: ")) * .01

                    change_owed = inserted_money(
                        quarters, dimes, nickels, pennies) - MENU[choice]["cost"]

                    if inserted_money(quarters, dimes, nickels, pennies) < MENU[choice]["cost"]:
                        print(
                            "Sorry, you didn't insert enough change. Your money was returned.")
                        accepting_money = False
                    else:
                        use_resources(choice)
                        print(
                            f"Here is {'${:,.2f}'.format(change_owed)} in change.")
                        print(f"Here is your {choice} ☕️. Enjoy!")
                        accepting_money = False
                        # machine_running = True
                        awaiting_drink = True


game()

# coffee machine (instructor solution)
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
