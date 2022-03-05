# Congratulations you have just gotten a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
#     Small Pizza: $ 15
#     Medium Pizza: $ 20
#     Large Pizza: $ 25

#     Pepperoni for Small Pizza: +$2
#     Pepperoni for Medium or Large Pizza: +$3

#     Extra Cheese for any size pizza: +$1

# Pizza Order Steps.
    # 1. Ask for size
    # 2. Ask if they want pepperoni
    # 3. Ask if they want extra cheese
    # 4. Calculate Total Bill

size = input("What size pizza do you want? S, M or L?")
add_pepperoni = input("Do you want Pepperoni? Y or N?")
extra_cheese = input("Do you want extra cheese? Y or N?")

bill = 0

# Calculate Size Price
if size == "S" or "s":
    bill += 15

elif size == "M" or "m":
    bill += 20

elif size == "L" or "l":
    bill += 25

# Add pepperoni
if add_pepperoni == "Y" or "y":
    if size == "S" or "s":
        bill += 2
    elif size == "M" or "m" or "L" or "l":
        bill += 3

# Add Cheese
if extra_cheese == "Y" or "y":
    bill +=1

print(f"Your final bill is ${bill}")