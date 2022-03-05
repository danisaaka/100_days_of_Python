# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill

import random
# Split String Method
# This method is used to generate a list from the input.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# The len function can be used to determine the number of characters in a string or the number of elements in a list/object
num_items = len(names)

# The line below means that we are using the len function minus one to get an offset value from the list
random_choice  = random.randint(0,(num_items-1))

# code to generate a random person from the list
person_to_pay = names[random_choice]

print(person_to_pay + " is going to buy the meal today ")

# Shorter Code alternative
# Using random choice method

person_to_pay = random.choice(names)
print(person_to_pay)