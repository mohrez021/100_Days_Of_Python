import string
import random

num_of_letters = int(input("How many letters would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like? "))
num_of_numbers = int(input("How many numbers would you like? "))

password = []
for _ in range(num_of_letters):
    password.append(random.choice(string.ascii_letters))

for _ in range(num_of_symbols):
    password.append(random.choice(string.punctuation))

for _ in range(num_of_numbers):
    password.append(random.choice(string.digits))

# shuffle the above password
random.shuffle(password)
print(''.join(password))