"""
Instructions
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.
Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output
171
Hint
    Remember to use the round() function to round the average height before you print it.
"""

num_of_students = 0
sum_of_heights = 0
student_heights = input("Enter height of students: ").split()
for height in student_heights:
    num_of_students += 1
    sum_of_heights += int(height)
avg_height = round(sum_of_heights / num_of_students)
print(avg_height)

"""
My code # but we should not use len() and sum() in this exercise, and we should use loop
student_heights = input("Enter height of your classmates: ").split()
number_of_students = len(student_heights)
for n in range(0, number_of_students):
    student_heights[n] = int(student_heights[n])
average_height = round(sum(student_heights) / number_of_students)
print(average_height)
"""

"""
Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output
171
"""
