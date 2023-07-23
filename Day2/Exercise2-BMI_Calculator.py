'''
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person \
    both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
Warning you should convert the result to a whole number.
Example Input
weight = 80
height = 1.75
Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837
26
'''
print("BMI:\
      \n\tUnderweight: BMI < 18.5\
      \n\tNormal weight: BMI 18.5-25\
      \n\tOverweight: BMI 25-30\
      \n\tObese: BMI > 30\n\
      ")
weight = int(input("Enter your weight in KG: "))
height = float(input("Enter your height in meter: "))
BMI = weight / (height ** 2)
print(f"{weight} ÷ ({height} * {height}) = {BMI}\n{int(BMI)}")
