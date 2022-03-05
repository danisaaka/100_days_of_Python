# Write a program taht works out whether if a given year is a leap year.

print("This programs asks a user to input a year andcheck whether it is a leap year or not.")
year = int(input("Which year did you want to check?\n"))

if year % 400 == 0:
    print(f"You entered the year {year}, and it is a leap year.")
elif year % 100 == 0:
    print(f"You entered the year {year}, and it is a leap year.")
elif year % 4 == 0:
    print(f"You entered the year {year}, and it is a leap year.")
else:
    print(f"You entered the year {year}, and it is not a leap year.")
