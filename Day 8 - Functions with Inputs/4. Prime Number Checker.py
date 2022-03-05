# You will need to  write a function that checks whether if the number passed into it is a prime number or not.

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"You input {number} to be checked\nIt is a Prime Number")
    else:
        print(f"You input {number} to be checked\nIt is NOT a prime number")

n = int(input("Check this number:\n"))
prime_checker(number=n)