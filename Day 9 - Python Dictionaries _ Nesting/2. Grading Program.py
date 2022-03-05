# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the vaues are their exam scores
# Write a porgram that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

student_scores = {
    "Harry": 81,
    "Ron":78,
    "Hermoine":99,
    "Draco":74,
    "Neville":62
}

# TO-DO 1: Create an empty dictionary called student_grades.
student_grades = {}

# TO-DO 2: Write your code below to add the grades to student grades
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Test your code
print(student_grades)