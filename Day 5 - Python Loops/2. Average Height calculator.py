# You are going to write a program that calculates teh average student height from a List of heights.
#  average_height = sum of heights / total number of heights.

student_heights = input("Input a list of student heights:\n").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

# start a counter from zero to add up the items in the list
total_height = 0
for height in student_heights:
    total_height += height

# use a for loop to count the number of items in the list. The code will keep on running for as many items there are in the list.
number_of_students = 0
for student in student_heights:
    number_of_students +=1

average_height = total_height/number_of_students
print(total_height)
print(number_of_students)
print(average_height)