# Write a program that calculates teh Body Mass Index from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. BMI is calculated by dividing a person's weight in kilograms by the square of their height in metres.

# BMI = Weight/(Height)^2
# You should convert the result to a whole number

height = input("Enter your height in metres:\n")
weight = input("Enter your weight in kilograms:\n")

# convert the height and weight into integers to calculate BMI
height_int = float(height)
weight_int = float(weight)
BMI = (weight_int/(height_int **2))
BMI_int = int(BMI)

# display output
print("You input a weight of " + weight + "kg and a  height of " + height + "m.")
print("BMI = Weight/(Height)^2")
print( weight + " / " + "(" + height + "x" + height + ") = " + str(BMI) )
print(BMI_int)



