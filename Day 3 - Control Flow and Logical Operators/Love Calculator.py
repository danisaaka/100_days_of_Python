# You are going to write a program that tests compatibility between 2 people.
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_string = name1 + name2
lowercase_string = combined_string.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score}, you go togethr like coke and mentos ")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")    
