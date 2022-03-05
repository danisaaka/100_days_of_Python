# Make a rock, paper, scissors game.
# Start the game by asking the player: "What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors"
# From there you will need to figure out:
#   how you will store teh user's input?
#   how you will generate a random choice for the computer?
#   how you will compare the user's and the computer's choice to determin the winner or draw?
#   how you will give feedback to the player?


# import the random library first.
import random

# ASCII diagrams for the animations.

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper =('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

''')

scissors =('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')
# game_images combines all the ASCII into 1 list. 
game_images = [rock, paper, scissors]   

# Ask the user to choose betwwn rock, paper or scissors
user_choice = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer Chose: ")
    print(game_images[computer_choice])


    if user_choice ==  0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw")

# LOGIC HERE:
# 1. Create a list with the animations
# 2. Design the game logic. rock-paper-scissors
# 3. The first condition is that the user MUST key in a value  within randint(0,2). Check line 50