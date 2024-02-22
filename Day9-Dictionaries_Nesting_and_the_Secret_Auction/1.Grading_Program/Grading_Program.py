student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student]  <= 70:
        result = "Fail"
    elif student_scores[student] <= 80:
        result = "Acceptable"
    elif student_scores[student] <= 90:
        result = "Exceeds Expectations"
    elif student_scores[student] <= 100:
        result = "Outstanding"
    student_grades[student] = result
    
    
    

# 🚨 Don't change the code below 👇
print(student_grades)
