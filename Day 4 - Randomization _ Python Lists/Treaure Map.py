# You are going to write a program which will mark a spot with an X
# In the starting code you will find a variabel called map. This map contains a nested list.
# In the starting list we have used new line (\n) to format the three rows into a square
# YOur job is to write a program taht allows you to mark a square on the map using a 2 digit system. 

row1 = ["A","B","C",]
row2 = ["D","E","F"]
row3 = ["G","H","I"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

# write your code from here
horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = "x"

print(f"{row1}\n{row2}\n{row3}")