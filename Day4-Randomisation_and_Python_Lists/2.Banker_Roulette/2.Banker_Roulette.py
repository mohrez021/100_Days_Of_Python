import random

names = input("Enter the names: (e.g. name, name, name)\n").replace(" ", "")

list_of_names = names.split(sep=",")

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
