########## Randomisation ##########
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# import random
### generate random integer number between two numbers ###
# import random
# print(random.randint(1, 10))

### generate random floating point number between 0 and 1.  random.random():     0 <= random_float < 1 ###
# import random
# print(random.random())

### generate random floating point number between a and b. random.uniform(a, b):     a <= random_float <= b ###
# import random
# print(random.uniform(0, 10))

# --------------------------------------------------------------- -------------------------------------------#

########## module ##########
### in this directory I have main.py and my_module.py . I can import my_module.py in my main.py app. ###

# ----------------------------------------------------------------------------------------------------------#

########## Lists ##########
### https://docs.python.org/3/tutorial/datastructures.html ###
### use list to store many pieces of related data but they also have an order base the location of items in the list. ###
# list_of_items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10", "item11",
#                 "item12", "item13", "item14", "item15", "item16", "item17", "item18", "item19", "item20"
#                 ]
# print(list_of_items)
# print(list_of_items[0])     # => item1
# print(list_of_items[-2])    # => item19
# print(list_of_items[::-1])    # => reverse the list (just show not change)
# print(list_of_items[-1])    # => item20 (last item)
# print(len(list_of_items))    # => number of items in list
# print(list_of_items[len(list_of_items) - 1])    # => item20 (last item)

# list_of_items[0] = "new_item1"  # change the first value in list
# print(list_of_items)
# add new_item21 at the end of list (just one value)
# list_of_items.append("new_item21")
# print(list_of_items)
# add a list items (a bunch of values) at the end of the list
# list_of_items.extend(["new_item22", "new_item23", "new_item24"])
# print(list_of_items)
# print(random.choice(list_of_items))     # => randomly select an item in list   random.choice(list)

### Nested lists: List in List ###
# old_list = ["item1", "item2", "item3"]
# new_list = ["new_item1", "new_item2", "new_item3", "new_item4"]
# mixed_list = [new_list, old_list]
# => output: [['new_item1', 'new_item2', 'new_item3', 'new_item4'], ['item1', 'item2', 'item3']]
# print(mixed_list)
# => output: [['new_item1', 'new_item2', 'new_item3', 'new_item4']]
# print(mixed_list[0])
# => output: new_item2
# print(mixed_list[0][1])
