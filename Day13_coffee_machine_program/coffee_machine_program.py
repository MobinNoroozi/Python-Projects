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

PROFIT = 0 

# Generates a report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: {PROFIT}")


def check_enough_resource(chosen_drink_ingridient): 
    for item in chosen_drink_ingridient: # For each item in the ingridient list, it checks if we have enough
        if (resources[item] >= chosen_drink_ingridient[item]):
            pass
        else:
            print(f"Sorry there is not enough {item}.") # If we do not have enough we tell them what is missing and return false
            return False
    return True # If we do have enough of all needed ingridients, then we return true

# Take payments
def insert_payment():
    quarters = int(input("Insert number of quarters: "))
    dimes = int(input("Insert number of dimes: "))
    nickles = int(input("Insert number of nickles: "))
    pennies = int(input("Insert number of pennies: "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total # Total money inserted


def check_enough_money_inserted(total, drink):
    global PROFIT
    drink_cost = drink["cost"]

    if (drink_cost > total): # Not enough money is inserted
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    elif(drink_cost == total): # Exact change
        PROFIT += total
        return True
    
    else: # Money inserted is more than the drink cost, we need to refund some
        PROFIT += drink_cost
        #change = (total - drink_cost)
        rounded_change = round(total-drink_cost, 2)
        print(f"Here is ${rounded_change} dollars in change.")
        return True


def make_coffee(chosen_drink_ingridient):
    for item in chosen_drink_ingridient: # We suntract the needed ingridient to make coffee from the resources
        resources[item]-= chosen_drink_ingridient[item]


def add_resources():
    for item in resources:
        want = input(f"Would you like to add {item}? 'y' or 'n': ").lower()
        if want == "y":
            resources[item] += int(input(f"How much {item} do you want to add? "))
        


machine_is_on = True
while(machine_is_on):
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if(user_choice == "off"):
        machine_is_on = False #Turns off the machine 

    elif user_choice == "report":
        print_report() #Generate the report
    
    elif user_choice == "fill":
        print_report()
        add_resources()
        print_report()

    elif user_choice in MENU: 
        drink_name = MENU[user_choice] #If they choose a proper drink, then we get its name which is a dictionary

        chosen_drink_ingridient = drink_name["ingredients"] #We get the ingridients of the drink which is a dictionary

        if(check_enough_resource(chosen_drink_ingridient)) == True: # We check if we have enough resources, if not tell them not enough resources in the function, and go again
            total = insert_payment() # If we do, we take payment

            if(check_enough_money_inserted(total, drink_name) == True): # If enough money inserted, we proceed with making coffee, if not, we tell them, we refund themm and go again.
                print_report() # Generate report before making coffee
                make_coffee(chosen_drink_ingridient) # We make the coffee, and use the ingridients 
                print(f"Here is your {user_choice}. Enjoy!!")
                print_report() # Generate a report after making the coffee

    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")
