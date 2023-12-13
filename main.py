from menu import *


# TODO check for sufficient resources
machine_resources = resources

# TODO process coins
def calculate_coins():
    pass

# TODO check if transaction is successful
def process_transactions():
    pass

# TODO print report of available resources
def display_resources():
    for key in machine_resources:
        print(f"{key}: {machine_resources[key]}")

# TODO ability to turn off coffee machine

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

def main():
    machine_on = True
    # TODO ask user to for latte
    while machine_on:
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
        while valid_request(request) is False:
            print(f"\n\"{request}\" is not a valid request, please try again")
            request = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if request == 'exit':
            machine_on = False
            
        elif request == 'resources':
            display_resources()
    # TODO check for valid resource

main()