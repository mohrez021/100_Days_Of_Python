from os import name,system
from art import logo, welcome

print(logo, welcome)
running_os = name
contributers = {}

    
def clean_screen():
    match running_os:
        case 'nt':
            system('cls')
        case 'posix':
            system('clear')

def get_info():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    contributers[name] = bid

def check_winner():
    winner_name = max(contributers, key=contributers.get)
    winner_bid = contributers[winner_name]
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

while True:
    get_info()
    check = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    match check:
        case "yes":
            clean_screen()
            continue
        case "no":
            check_winner()
            break
