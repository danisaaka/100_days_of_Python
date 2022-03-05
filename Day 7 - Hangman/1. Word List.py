# Step 1
import random
word_list = ["aardvark","baboon","camel"]

# TO-DO-1 - Randomly choose a word from the word list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# TO-DO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case.
guess = input("Please guess a letter:\n").lower()


# TO-DO 3 - Check if the letter the user guessed is one of the letters in the chosen word.
print(f"The chosen_word is {chosen_word}")
for letter in chosen_word:
    if letter == guess:
        print("correct")
    else:
        print("wrong")


