# You are going to write a program taht calculates the highest score from a list of scores
# You are not allowed to use the max or min function.

student_scores = input("Input a list of student scores: \n").split()

for student_score in range(0, len(student_scores)):
    student_scores[student_score] = int(student_scores[student_score])

heighest_score = 0
for score in student_scores:
    if score > heighest_score:
        heighest_score = score

print(f"The heighest score in the class is: {heighest_score}")
