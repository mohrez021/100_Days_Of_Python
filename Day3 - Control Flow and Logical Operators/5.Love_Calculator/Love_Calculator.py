############## way1 ##############
digit_1 = 0
digit_2 = 0
score = 0

name_1 = input("Enter your name: ")
name_2 = input("Enter your crush name: ")
both_name = (name_1 + name_2).lower()

for letter in both_name:
    digit_1 += "true".count(letter)
    digit_2 += "love".count(letter)

score = int(str(digit_1) + str(digit_2))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}%.")


############## way2 ##############
'''
digit_1 = 0
digit_2 = 0

name_1 = str.lower(input("Enter the name of first person: "))
name_2 = str.lower(input("Enter the name of second person: "))

for letter in name_1:
    if (letter in "true"):
        digit_1 += 1
    if (letter in "love"):
        digit_2 += 1

for letter in name_2:
    if (letter in "true"):
        digit_1 += 1
    if (letter in "love"):
        digit_2 += 1

total_score = int(str(digit_1) + str(digit_2))

if total_score < 10 or total_score > 90:
    print(
        f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score =< 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}%.")
'''
