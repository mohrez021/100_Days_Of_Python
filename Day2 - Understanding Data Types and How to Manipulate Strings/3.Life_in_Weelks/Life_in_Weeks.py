'''
Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
    You have x days, y weeks, z months, and i years left.
Where x, y, z and i are replaced with the actual calculated numbers.
There are 365 days in a year, 52 weeks in a year and 12 months in a year.
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
Example Input
56
Example Output
You have 21535 days, 2832 weeks, 708 months, and 59 years left.
'''
age = int(input("How old are you? "))
age_life = 90

remain_years = age_life - age
remain_months = remain_years * 12
remain_weeks = remain_years * 52
remain_days = remain_years * 365

print(f"You have {remain_days} days, {remain_weeks} weeks, {remain_months} months, and {remain_years} years left.")
