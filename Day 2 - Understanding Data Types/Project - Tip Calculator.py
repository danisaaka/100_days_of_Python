print("Welcome to the Tip Calculator!!")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give?\n10%, 12%, or 15%?\n"))

total_bill = bill + (bill * (tip/100))

# prompt for number of people
people = int(input("How many people will be splitting the bill?\n"))
individual_bill = round(total_bill/people,2)
individual_bill = "{:.2f}.".format(individual_bill)

# display output
print(f"Each person should pay ${individual_bill}")