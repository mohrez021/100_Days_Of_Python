age = int(input("How old are you? "))
age_life = 90

remain_years = age_life - age
remain_months = remain_years * 12
remain_weeks = remain_years * 52
remain_days = remain_years * 365

message = f"You have {remain_days} days, {remain_weeks} weeks, {remain_months} months, and {remain_years} years left."
print(message)
