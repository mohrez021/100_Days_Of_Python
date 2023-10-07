from welcome import welcome

print(welcome())
choice1 = input(
    'You\'re at a cross road. where do you want to go? Type "left" or "right"\n').lower()

if choice1 != "left":
    result = "You fell into a hole.\nGame Over!"
else:
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat \
            or type "swim" to swim across.\n').lower()
    if choice2 != "wait":
        result = "You got attacked by an angry crocodile.\nGame Over!"
    else:
        choice3 = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue".\
                Which color do you choose?\n').lower()
        if choice3 == "yellow":
            result = "You found the treasure!\nYou Win!"
        elif choice3 == "red":
            result = "It's a room full of fire.\nGame Over!"
        elif choice3 == "blue":
            result = "You enter a room of beasts.\nGame Over!"
        else:
            result = "You choose a door that doesn't exist.\nGame Over!"

print(result)
