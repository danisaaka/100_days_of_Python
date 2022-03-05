# Write a program that works out ifa given number is an odd or even number.

# Welcome Screen & App Info
print("This a program to check the whether the user's input is an odd or even number.")
number = int(input("Which number do you want to check? "))

# Code to determine if number is an odd or an even number

if number % 2 == 0:
    print(f" The number you input was {number}, this is an even number.")

elif number % 2 !=0:
    print(f" The number you input was {number}, this is an odd number.")
