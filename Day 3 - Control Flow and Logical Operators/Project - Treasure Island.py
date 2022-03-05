print('''
████████ ██████  ███████  █████  ███████ ██    ██ ██████  ███████     ██ ███████ ██       █████  ███    ██ ██████  
   ██    ██   ██ ██      ██   ██ ██      ██    ██ ██   ██ ██          ██ ██      ██      ██   ██ ████   ██ ██   ██ 
   ██    ██████  █████   ███████ ███████ ██    ██ ██████  █████       ██ ███████ ██      ███████ ██ ██  ██ ██   ██ 
   ██    ██   ██ ██      ██   ██      ██ ██    ██ ██   ██ ██          ██      ██ ██      ██   ██ ██  ██ ██ ██   ██ 
   ██    ██   ██ ███████ ██   ██ ███████  ██████  ██   ██ ███████     ██ ███████ ███████ ██   ██ ██   ████ ██████  
                                                                                                                   
                                                                                                                   
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("Do you want to go left or right?\nType Left or Right\n").lower()

if left_or_right == "left":
    swim_or_wait = input("You have come to a lake. There is an island in the middle of the lake.\nDo you want to swim across or wait for a boat?\nPlease type your choice\n").lower()
else:
    print("You fell into a hole:\n GAME OVER.\nTry Again.")

if swim_or_wait =="wait":
    which_door = input("Which door do you choose? Red, Blue or Yellow?\nType the color door you choose\n").lower()
else:
    print("You were attacked by a trout.\nGAME OVER.\nTry Again.")

if which_door == "yellow":
    print('''Congratulations! You found the treasure!
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')

elif which_door == "red":
    print("You chose the red door.\nYou were burned by fire.\nGame Over.")
elif which_door == "blue":
    print("You chose the blue door.\nYou were eaten by beasts.\nGame Over.")
else:
    print("Incorrect choice.\nGame Over.")