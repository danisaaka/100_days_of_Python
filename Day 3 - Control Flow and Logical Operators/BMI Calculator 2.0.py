# Write a program that interprets the BMI based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
#  Under 18.5 = underweight
#  Over 18.5 but below 25 are normal weight
#  Over 25 but below 30 are slightly overweight
#  Over 30 but below 35 are obese
#  Above 35 are clinically obese

height = float(input("Enter your height in metres:\n"))
weight = float(input("Enter your weight in kg:\n"))
# BMI formula
BMI = round(weight/(height**2))

# BMI Classifiaction Code
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print("You are clinically obese.")