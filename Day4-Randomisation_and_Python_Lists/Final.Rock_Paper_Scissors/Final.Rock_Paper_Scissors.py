import random
from asci_art import asci

print(asci.logo)
print("Welcome to Rock, Paper, Scissors game.\
 Each player reach score 3 sonner, is winner. Have fun!")

computer_choices = [asci.rock, asci.paper, asci.scissors]
user_score = 0
computer_score = 0

while True:
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors or 'quit' for exit: ")
    computer_choice = random.choice(computer_choices)
    match user_choice:
        case "0":
            print(f"Your choice:\n{asci.rock}\nComputer choice:\n{computer_choice}")
        case "1":
            print(f"Your choice:\n{asci.paper}\nComputer choice:\n{computer_choice}")
        case "2":
            print(f"Your choice:\n{asci.scissors}\nComputer choice:\n{computer_choice}")
        case "quit":
            print("Bye")
            break
        case _:
            print("incorect choice!!!")
            continue

    combine_str = user_choice + str(computer_choices.index(computer_choice))
    # print(combine_str, type(combine_str))
    if combine_str == "12" or combine_str == "20" or combine_str == "01":
        computer_score += 1
    elif combine_str == "02" or combine_str == "10" or combine_str == "21":
        user_score += 1
    print(f"Your Score: {user_score}\nComputer Score: {computer_score}")
    
    if user_score >= 3 and user_score > computer_score:
        print("You win!")
        break
    if computer_score >=3 and computer_score > user_score:
        print("Game Over!")
        break 
