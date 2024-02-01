class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in meter: "))
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 30:
    result = "slightly overweight"
elif bmi < 35:
    result = "obese"
else:
    result = "clinically obese"

# bold string => \033[1m{var}\033[0m
bold_result = f"{color.BOLD}{result}{color.END}"

print(f"Your BMI is {bmi}, you are {bold_result}.")
