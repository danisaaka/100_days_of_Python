# You are going to write a virtual coin toss program. It will randomly tell the user Heads or Tails.

# import the random module
import random

# generate either 1 or 0 using the randint function
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")