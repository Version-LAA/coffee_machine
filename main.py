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

# TODO process coins
def calculate_coins(q,d,n,p):
    return ((q*.25)+(d*.10)+(n*.05)+(p*.01))

# TODO check if transaction is successful
def process_transactions():
    pass

# print report of available resources
def display_resources():
    for key in machine_resources:
        print(f"{key}: {machine_resources[key]}")



# TODO make coffee
def make_coffe():
    pass

# valid request
def valid_request(request):
    valid = ["espresso","latte","cappuccino","exit","resources"]
    if request in valid:
        return True
    else:
        return False
    
def new_request():
    request = input("""What would you like?
    - espresso 🍵
    - latte 🍶
    - cappuccino ☕️ 
                        
    Drink Choice: """).lower()
        
    # check for valid resource
    while valid_request(request) is False:
        print(f"\n\"{request}\" is not a valid request, please try again")
        request = input("""\nWhat would you like?
        - espresso 🍵
        - latte 🍶
        - cappuccino ☕️ 
                        
        Drink Choice: """).lower()
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

        elif request == 'resources':
            display_resources()
        else:
            if check_resources(request):
                # TODO request payment
                print(f"Drink Price: {MENU[request]['cost']}")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                
                # TODO process payment
                payment = calculate_coins(quarters,dimes,nickles,pennies)
                if payment >= MENU[request]["cost"]:
                    print("enough money")
                    process_transactions() # TODO - finish defining this function
                else:
                    print(f"not enough money - here is your refund of {payment}")
            else:
                print("Not enough resources to make drink of choice!")


    

main()