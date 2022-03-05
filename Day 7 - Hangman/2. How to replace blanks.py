import random
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"The solution is: {chosen_word}")

# TO-DO 1: create an empty list called display.
display = []

# For each letter in the chosen_word, add a "_" to display
for letter in range(word_length):
    display.append("_")

guess = input("Guess a letter:\n").lower()

# TO-DO 2: Loop through each position in the chosen word. IF the letter at the position matches 'guess' then reveal that letter 
# in the display at that position
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# TO-DO 3: Print display and you should see the guessed letter in the correct position and every other letter replaced with "_"
print(display)