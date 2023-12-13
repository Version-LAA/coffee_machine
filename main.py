from menu import *
import os


# check for sufficient resources
machine_resources = resources
def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for i in ingredients:
        if ingredients[i] > machine_resources[i]:
            return False
        else:
            return True

    print(ingredients)

# process coins
def calculate_coins(q,d,n,p):
    return ((q*.25)+(d*.10)+(n*.05)+(p*.01))

# check if transaction is successful
def process_transactions(drink,payment):
    # take the total drink cost and subtract payment
    # if drink cost == payment:
      ## refund == 0
      ## add payment to system resources
    #else:
      ## refund = drink cost - payment
      ## add payment to system
    drink_cost = drink['cost']
    if drink_cost == payment:
        drink_profit = payment
        return drink_profit
    else:
        change = "{:.2f}".format(abs(drink_cost - payment))
        print(f"Your change is: ${change}")
        drink_profit = drink_cost
        return drink_profit


# print report of available resources
def display_resources():
    print("System Resources:")
    for key in machine_resources:
        print(f"- {key}: {machine_resources[key]}")



# make coffee
def make_coffe(drink,machine_resources):
    drink_ingredients = drink['ingredients']
    for i in drink_ingredients:
        machine_resources[i] -= drink_ingredients[i]
    return machine_resources
    

# valid request
def valid_request(request):
    valid = ["espresso","latte","cappuccino","exit","report"]
    if request in valid:
        return True
    else:
        return False
    
def new_request():
    request = input("\nWhat would you like? espresso 🍵 / latte 🍶 /cappuccino ☕️: ").lower()
        
    # check for valid resource
    while valid_request(request) is False:
        print(f"\n\"{request}\" is not a valid request, please try again")
        request = input("\nWhat would you like? espresso 🍵 / latte 🍶 /cappuccino ☕️: ").lower()
    return request

def main():
    os.system("clear")
    machine_on = True
    # ask user to for latte
    while machine_on:
        request = new_request()
        if request == 'exit':
            # ability to turn off coffee machine
            machine_on = False

        elif request == 'report':
            print("\n")
            display_resources()
        else:
            if check_resources(request):
                # request payment
                print(f"Drink Price: {MENU[request]['cost']}")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                
                # process payment and make coffee
                payment = calculate_coins(quarters,dimes,nickles,pennies)
                drink = MENU[request]
                if payment >= drink["cost"]:
                    profit = process_transactions(drink,payment)
                    if 'money' in machine_resources:
                        machine_resources['money'] += profit
                    else:
                        machine_resources['money'] = profit
                    make_coffe(drink,machine_resources)
          
    
                else:
                    print(f"not enough money - here is your refund of {payment}")
            else:
                print("Not enough resources to make drink of choice!")


    

main()