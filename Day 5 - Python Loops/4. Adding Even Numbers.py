total_sum = 0

for number in range(1,101):
    if number % 2 == 0:
        print(number)
        total_sum += number

print(total_sum)