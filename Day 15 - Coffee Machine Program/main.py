from data import resources, MENU

# 1. Prompt user by asking "What would you like> (espresson/latte/cappucino)"
machine_off = False
while  machine_off != True:
    user_choice = input("What would you like to order?\nEspresso / Latte / Cappuccino.\n").lower()

    # Check the user's input to decide what to do next.
    # The prompt should show every time action has completed. The prompt should show again to serve the next customer
    # Turn off the Coffee Machine by entering "off" to the prompt
    # For maintainers of the coffee machine, they can use "off" 
    # as the secret word to turn off the machine.
    if user_choice == "off":
        machine_off = True
        print("machine will now turn off")
    elif user_choice == "report":
        print("This will display report")
    else:
        print("The program continues to run")
    # How will I break the loop if incorrect input is entered?


    
# 3. Print report.
    # When the user enter's "report" to the prompt, a report should be generated that shows the current resource value
def resources_left():
    print()
# 4. Check resources sufficient
    # When the user chooses a drink, the program should check if there are enough resources to make that drink.
    
# 5. Process coins
def process_coins():
    # If there are insufficient resources to make teh drink selected, then the program should prompt the user to insert coins
    # quarters = 0.25, dimes = 0.10, nickles = 0.05, pennies = 0.01
    nr_quarters = int(input("How many quarters?\n"))
    nr_dimes = int(input("How many dimes?\n"))
    nr_nickels = int(input("How many nickles"))
    
    # Calculate the monetary value of the coins inserted

# 6. Check transaction successful?
    # Check that the user has inserted enough money to purchase the drink they selected.
    # If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and thus will be reflected the
    # next time "report" is triggered
    # If the user has inserted too much money, teh machine should offer change. The change shoudl be rounded to 2 decimal places
    
# 7. Make Coffee.
    # If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the 
    # drink should be deducted from the coffee machine resources.
    # Once all ingredients have been deducted, tell the user "Here is your latte. Enjoy!" If latte was their choice of drink and so on.
