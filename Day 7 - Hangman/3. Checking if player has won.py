import random
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"The solution is: {chosen_word}")

# Create blanks
display = []
for letter in range(word_length):
    display.append("_")

# Use a While loop to let the user guess again. The loop should only stop once the user has guessed all the 
# letters in the chosen word and display has no more blanks
end_of_game = False

while not end_of_game:      
        guess = input("Guess a letter:\n").lower()

        # check guessed letters
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(display)
        if "_" not in display:
            end_of_game = True
            print("You win!")