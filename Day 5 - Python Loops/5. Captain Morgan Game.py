
for number in range(0,101):
    if number % 5 == 0 and number % 3 == 0:
        print("Captain Morgan")
    elif number % 5 == 0:
        print("Morgan")
    elif number % 3 == 0:
        print("Captain")
    else:
        print(number)