# way 1
# Loading alphabet, digit, and symbol to list and select from them randomly
import random
import string

# Default parameters
pass_length = 14
num_of_symbols = 4
num_of_digits = 4
password_list = []

# create three list of different character type (alphabet, digit, symbol)
letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to PyPassword Generator!")
print(f"Default parameters: pass_length={pass_length}, num_of_symbols={num_of_symbols}, num_of_digits={num_of_digits}")
change_parameters = input("Do you want change default parameters? (y/n): ")

if change_parameters == "y":
    pass_length = int(input("Password Length: "))
    num_of_symbols = int(input("Number of Symbols: "))
    num_of_digits = int(input("Number of Digits: "))
else:
    pass

# run the loop until to define num_of_symbols
for symbol in range(num_of_symbols):
    password_list.append(random.choice(symbols))
for digit in range(num_of_digits):
    password_list.append(random.choice(digits))
for alphabet in range(pass_length - (num_of_symbols + num_of_digits)):
    password_list.append(random.choice(letters))

# reorder the list items. shuffle it
random.shuffle(password_list)

# return the list items to string and concatenate them
password = ""
for char in password_list:
    password += char

# print(password_list)
print(password)

"""
# way 2
# Loading alphabet, digit, and symbol to list and select from them randomly
import random
import string

# Default parameters
pass_length = 14
num_of_symbols = 4
num_of_digit = 4
password = ""

# create three list of different character type (alphabet, digit, symbol)
letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to PyPassword Generator!")
print(f"Default parameters: pass_length={pass_length}, num_of_symbols={num_of_symbols}, num_of_digits={num_of_digit}")
change_parameters = input("Do you want change default parameters? (y/n): ")

if change_parameters == "y":
    pass_length = int(input("Password Length: "))
    num_of_symbols = int(input("Number of Symbols: "))
    num_of_digit = int(input("Number of Digits: "))
else:
    pass

# run the loop until to define num_of_symbols
selected_symbols = ''.join((random.choice(symbols)) for x in range(num_of_symbols))
# run the loop until to define number_of_digits
selected_digits = ''.join((random.choice(digits)) for x in range(num_of_digits))
# run the loop until to define remain characters
selected_alphabets = ''.join((random.choice(letters)) for x in range((pass_length - (num_of_symbols + num_of_digit))))

# concatenate strings together and shuffle the order of string
password = ''.join(random.sample(selected_alphabets + selected_digits + selected_symbols, k=pass_length))
print(password)
"""

