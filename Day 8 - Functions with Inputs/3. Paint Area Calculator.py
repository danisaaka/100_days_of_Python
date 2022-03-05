# You are painting a wall. The instructions on the apint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you will ned to buy.

import math

def paint_calc(height,width,cover):
    area = height * width
    nr_cans = math.ceil(area/cover)
    print(f"You will need {nr_cans} cans of paint")

test_h = int(input("What is the height of teh wall?\n"))
test_w = int(input("What is the width of the wall?\n"))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)





