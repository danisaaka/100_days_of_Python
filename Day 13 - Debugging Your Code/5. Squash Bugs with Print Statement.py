############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

#Print is Your Friend
pages = 0
print(f"line 22 {pages}")
word_per_page = 0
print(f"line 31: {word_per_page}")
pages = int(input("Number of pages: "))
print(f"line 33: {pages}")
word_per_page = int(input("Number of words per page: "))
print(f"line 35: {word_per_page}")
total_words = pages * word_per_page
print(f"the number of pages is {pages} and the number of words per page is {word_per_page}\nTotal Words = {pages} * {word_per_page} = {total_words}")
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])