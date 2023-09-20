print("BMI:\
      \n\tUnderweight: BMI < 18.5\
      \n\tNormal weight: BMI 18.5-25\
      \n\tOverweight: BMI 25-30\
      \n\tObese: BMI > 30\n\
      ")
weight = int(input("Enter your weight in KG: "))
height = float(input("Enter your height in meter: "))
BMI = weight / (height ** 2)
print(f"{weight} ÷ ({height} * {height}) = {BMI}\n{round(BMI)}")
