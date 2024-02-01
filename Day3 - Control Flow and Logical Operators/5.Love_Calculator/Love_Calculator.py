############## way1 ##############
num1 = 0
num2 = 0

name1 = input("Enter your name: ")
name2 = input("Enter your crush name: ")


name = (name1 + name2).lower()
for c in "true":
  num1 += name.count(c)

for c in "love":
  num2 += name.count(c)

num = int(str(num1) + str(num2))

if num < 10 or num > 90:
  print(f"Your score is {num}, you go together like coke and mentos.")
elif num > 40 and num < 50:
  print(f"Your score is {num}, you are alright together.")
else:
  print(f"Your score is {num}.")

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
