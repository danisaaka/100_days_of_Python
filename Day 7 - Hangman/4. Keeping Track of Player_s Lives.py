import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

# Create a variable called lives to keep track of the number of lives left left. Set lives = 6
no_of_lives = 6

# Testing code
print(f"The solution is: {chosen_word}")

# Create blanks
display = []
for letter in range(word_length):
    display.append("_")

while not end_of_game:      
        guess = input("Guess a letter:\n").lower()

        # check guessed letters
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        
        # If guess is not a letter in the chosen word, then reduce the number of lives by 1
        # If lives goes down to 0 then the game should stop and should print "You lose."
        if guess not in chosen_word:
            no_of_lives -= 1
            if no_of_lives == 0:
                end_of_game = True
                print("You lose.")

        # Join all the elements in the lust and turn it into a string.
        print(f"{''.join(display)}") 
        

        
        if "_" not in display:
            end_of_game = True
            print("You win!")
        print(stages[no_of_lives])