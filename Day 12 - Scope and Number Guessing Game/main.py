import random
import art

EASY_LEVEL_TURNS = 15
HARD_LEVEL_TURNS = 9

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You win. The number was {answer}")

def set_dificulty():
    level = input("Choose a difficulty\ntype either 'easy' or 'hard'\n").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(art.logo)
    print("Welcome to the number guessing game.")
    answer = random.randint(1,100)
    turns = set_dificulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left.")
        guess = int(input("Make a guess:\n"))
        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print(f"You ran out of lives.\nGame Over.\nThe correct answer was {answer}")
            return
        elif guess != answer:
            print("Try again.\n")

game()