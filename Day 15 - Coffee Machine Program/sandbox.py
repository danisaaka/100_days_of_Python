def process_coins():
    # If there are insufficient resources to make the drink selected, then the program should prompt the user to insert coins
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    
    nr_quarters = int(input("How many quarters?\n"))
    nr_dimes = int(input("How many dimes?\n"))
    nr_nickels = int(input("How many nickles\n"))
    nr_pennies = int(input("How many pennies?\n"))
    
    monetary_value = round((quarters*nr_quarters) + (dimes*nr_dimes) + (nickels * nr_nickels) + (pennies*nr_pennies),2)
    return monetary_value
    
process_coins()