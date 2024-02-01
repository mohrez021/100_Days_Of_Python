"""
Instructions
You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
    The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output
The highest score in the class is: 91
Hint
  Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?
"""
# way 1. which is right for this course and its purpose
highest_number = 0
student_scores = input("Enter student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if highest_number < student_scores[n]:
        highest_number = student_scores[n]
print(f"The highest score in the class is: {highest_number}")

"""
# way 2
student_scores = input("Enter student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
student_scores_sorted = student_scores.sort()
max_number = student_scores.pop()
print(f"The highest score in the class is: {max_number}")
"""

"""
# Way 3. My code: But we cannot use max() function so ignore this.
student_scores = input("Enter student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
max_number = max(student_scores)
print(f"The highest score in the class is: {max_number}")
"""

