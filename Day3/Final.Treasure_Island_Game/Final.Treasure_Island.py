'''
Tresure_Island
https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
https://ascii.co.uk/art/treasure

Inspired from a treasure island book, It is a simple text based game to find a treasure. able to create thanks to MLH live session.
What it does
    It asked for user input to left or right. After that on the user choice go to next stage of game.
    From second stage user get 2 option to choose waiting for a boat or swimming toward the island.
    From third stage user get 3 option to choose the door to get to trasure only one of the door is right option.Let Have a Fun!! 😁🎯.

'''
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
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
