'''
Instructions
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.
Example Output
Michael is going to buy the meal today!
Hint
    You might need the help of the len() function.
    https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
    Remember that Lists start at index 0!
'''

import random

# create a list from input values you must enter all the names as names followed by comma then space. e.g. name, name, name
# replace(" ", "") => means remove all spaces
names = input("Enter the names: (e.g. name, name, name)\n").replace(" ", "")

# split(sep=",") => seperate eacb item base on "," and create a list of items
list_of_names = names.split(sep=",")

# len(list) => give us number of items in list. len("string") => give us number of characters of "string"
num_items = len(list_of_names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = list_of_names[random_choice]
print(f"{person_who_will_pay} is going to buy the meal today!")


'''
# Better way (but we would like to use above solution in order to learn)
import random
names = input("Enter the names: (e.g. name, name, name)\n").replace(" ", "")
list_of_names = names.split(sep=",")
person_who_will_pay = random.choice(list_of_names)
print(f"{person_who_will_pay} is going to buy the meal today!")
'''
