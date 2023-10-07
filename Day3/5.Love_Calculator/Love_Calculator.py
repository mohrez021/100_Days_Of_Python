'''
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
    Take both people's names and check for the number of times the letters in the word TRUE occurs. 
    Then check for the number of times the letters in the word LOVE occurs. 
    Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.
The testing code will check for print output that is formatted like one of the lines below:
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
Hint
    The lower() function changes all the letters in a string to lowercase.
    https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
    The count() function will give you the number of times a letter occurs in a string.ex:
    name = "alireza"
    print(name.count("a"))  => 2
    https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
'''

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

name_1 = str.lower(input("Enter the name of first persion: "))
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
