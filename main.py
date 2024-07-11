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

from collections import Counter
money = 0
profit_espresso = 0
profit_latte = 0
profit_cappuccino = 0

# If the user type 'report', print the report of the quantity of the resources
def format_money(quarter, dime, nickle, penny):
    quarter = float(quarter * 0.25)
    dime = float(dime * 0.10)
    nickle = float(nickle * 0.05)
    penny = float(penny * 0.01)

    # create a dict called money to store the coins values
    money = {'quarter': quarter, 'dime': dime, 'nickle': nickle,
             'penny': penny}

    # calculate the sum of the coins
    sum_coins = 0
    for i in money.values():
        sum_coins += i
    return sum_coins


def format_report(money):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    resources['water'] = water
    resources['milk'] = milk
    resources['coffee'] = coffee
    resources['money'] = money



    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"

def check_resources(user_coffee, resources):
    if user_coffee == 'espresso':
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")
            return False
        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return False
        else:
            #print("It has resources")
            return True
    elif user_coffee == 'latte':
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")
            return False
        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return False
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False
        else:
            #print("It has resources")
            return True
    elif user_coffee == 'cappuccino':
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")
            return False
        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return False
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False
        else:
            #print("It has resources")
            return True


def check_transaction(user_coffee, resources):
    if user_coffee == 'espresso':
        if resources['money'] < MENU['espresso']['cost']:
            if resources['money'] == 0:
                print("Sorry there is not enough money.")
                return False
            elif resources['money'] > 0:
                print("Sorry there is not enough money. Money refunded.")
                return False
        else:
            standard_resource = resources['money']
            espresso_cost = MENU['espresso']['cost']
            espresso_change = standard_resource - espresso_cost
            print(f"Here is ${round(espresso_change, 2)} dollars in change.")
            return True
    elif user_coffee == 'latte':
        if resources['money'] < MENU['latte']['cost']:
            if resources['money'] == 0:
                print("Sorry there is not enough money.")
                return False
            elif resources['money'] > 0:
                print("Sorry there is not enough money. Money refunded.")
                return False
        else:
            standard_resource = resources['money']
            latte_cost = MENU['latte']['cost']
            latte_change = standard_resource - latte_cost
            print(f"Here is ${round(latte_change, 2)} dollars in change.")
            return True
    elif user_coffee == 'cappuccino':
        if resources['money'] < MENU['cappuccino']['cost']:
            if resources['money'] == 0:
                print("Sorry there is not enough money.")
                return False
            elif resources['money'] > 0:
                print("Sorry there is not enough money. Money refunded.")
                return False
        else:
            standard_resource = resources['money']
            cappuccino_cost = MENU['cappuccino']['cost']
            cappuccino_change = standard_resource - cappuccino_cost
            print(f"Here is ${round(cappuccino_change, 2)} dollars in change.")
            return True


def make_coffee(user_coffee, resources):
    if user_coffee == 'espresso':

        espresso = MENU['espresso']['cost']
        #print(f"Espresso = {espresso}")


        resources['profit'] = espresso

        standard_resource = Counter(resources)
        #print(f"standard resources = {standard_resource}")
        espresso_ingredients = Counter(MENU['espresso']['ingredients'])
        transaction = standard_resource - espresso_ingredients
        #print(f"transaction IS = {transaction}")

        print(f"Here is your espresso. Enjoy!")

        water = transaction['water']
        milk = transaction['milk']
        coffee = transaction['coffee']
        espresso = transaction['profit']


        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        resources['profit'] = espresso


        return espresso

    elif user_coffee == 'latte':

        latte = MENU['latte']['cost']
        #print(f"Latte = {latte}")
        resources['profit'] = latte

        standard_resource = Counter(resources)
        latte_ingredients = Counter(MENU['latte']['ingredients'])
        transaction = standard_resource - latte_ingredients

        print(f"Here is your latte. Enjoy!")

        water = transaction['water']
        milk = transaction['milk']
        coffee = transaction['coffee']
        latte = transaction['profit']

        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        resources['profit'] = latte
        #print(f"resources = {resources}")

        return latte
    elif user_coffee == 'cappuccino':

        cappuccino = MENU['cappuccino']['cost']
        #print(f"Latte = {cappuccino}")
        resources['profit'] = cappuccino


        standard_resource = Counter(resources)
        cappuccino_ingredients = Counter(MENU['cappuccino']['ingredients'])
        transaction = standard_resource - cappuccino_ingredients

        print(f"Here is your cappuccino. Enjoy!")

        water = transaction['water']
        milk = transaction['milk']
        coffee = transaction['coffee']
        cappuccino = transaction['profit']

        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        resources['profit'] = cappuccino

        return cappuccino

want_coffee = True
profit = 0
while want_coffee:
    # Ask the user for the type of coffee to make
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()



    if user_coffee == 'report':
        report = format_report(profit)
        print(report)
        continue

    if user_coffee == 'off':
        break
    elif (user_coffee != 'espresso' and user_coffee != 'latte'
            and user_coffee != 'cappuccino'):
        print(f"Sorry. We don't make {user_coffee}. Please choose 'espresso', "
              f"'latte' or 'cappuccino'.")
        continue

    has_resource = check_resources(user_coffee, resources)

    if not has_resource:
        break

    quarter = int(input("Please insert coins.\nHow many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))

    money = format_money(quarter, dime, nickle, penny)

    format_report(money)
    has_transaction = check_transaction(user_coffee, resources)

    if not has_transaction:
        continue

    if user_coffee == "espresso":
        espresso = profit_espresso
        profit_espresso += make_coffee(user_coffee, resources)
        # print(f"Espresso = {espresso}")
        # print(f"Profit_espresso = {profit_espresso}")
    elif user_coffee == "latte":
        latte = profit_latte
        profit_latte += make_coffee(user_coffee, resources)
        # print(f"Latte = {latte}")
        # print(f"Profit_latte = {profit_latte}")
    elif user_coffee == "cappuccino":
        cappuccino = profit_cappuccino
        profit_cappuccino += make_coffee(user_coffee, resources)

    profit = profit_espresso + profit_latte + profit_cappuccino
    resources['profit'] = profit
    #print(f"Resources = {resources}")
    report = resources
    # print(f"Profit = {profit}")
    # print(f"Report = {report}")


# TODO: 1.Print a report
# Ask the user for the type of coffee to make
# If the user type 'report', print the report of the quantity of the resources
# TODO: 2. Check resources sufficient?
# Check if it has sufficient resources for the coffee chose
# TODO: 3. Process coins.
# If the resources are sufficient, insert coins
# TODO: 4. Check transaction successful?
# Check if the money inserted is sufficient. If it is the case, provide the amount of
# change.
# TODO: 4. Make Coffee
# If resources and money are sufficient, go ahead, make a coffee and ask the next type
# of coffee.
