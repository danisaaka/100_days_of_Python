# Create a program using maths and f-strings that tells us how many days, weeks, and months we have left if we live until 90 years old
# It will take your current age as the input and output a message with our time left in this format
# You have x days, y weeks and z months left.

age = input("What is your current age?\n")

age_as_int = int(age)
age_difference = 90 - age_as_int

#convert age difference into respective formats.
years = age_difference
weeks = age_difference * 52
days = age_difference * 365
months = age_difference * 12

# print output
print(f"You have {days} days, {weeks} weeks and {months} months left")