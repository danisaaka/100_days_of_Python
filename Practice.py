# Calculate a running sum

# A user will enter numbers that will be added to the sum and when a negative number is encountered, 
# stop adding numbers and write out the final result

# Set sum to zero
sum = 0
game_over = False

# Ask the user to give an input


while game_over != True:
    # Ask the user to give an input
    next_number = int(input("Please Key in the next number to be added:\n"))
    
    # If input is a negative number, the programs stops.
    if next_number < 0:
        game_over = True
        print(f"Program has quit. The total sum so far is {sum}")
    else:
        sum = sum + next_number

