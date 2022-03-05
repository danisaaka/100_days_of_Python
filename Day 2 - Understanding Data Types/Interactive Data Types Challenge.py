# Write a program that adds the digits in a 2 digit number.
# Do not change the first three lines of the main.py code

two_digit_number = input("Type a two-digit number:\n ")

# split the 2 digit number into individual numbers using Subscript Method
digit_1 = int(two_digit_number[0])
digit_2 = int(two_digit_number[1])
sum = digit_1 + digit_2

# output the sum of the numbers
print("You entered " + two_digit_number + " as your integer")
print(str(digit_1) + " + " + str(digit_2) + " = " + str(sum))