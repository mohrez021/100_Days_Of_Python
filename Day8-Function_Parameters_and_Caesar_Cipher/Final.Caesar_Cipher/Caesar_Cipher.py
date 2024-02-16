from string import ascii_lowercase
from art import logo
print(logo)

def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    if shift_amount > 26:
        shift_amount %= 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for c in start_text:
        if c not in ascii_lowercase:
            end_text += c
            continue
        position = ascii_lowercase.index(c)
        new_position = position + shift_amount
        if new_position > 25:
            end_text += ascii_lowercase[new_position - 26]
        else:
            end_text += ascii_lowercase[new_position]      

    print(f"The {cipher_direction}d text is {end_text}")   

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    answer = input("\nWould you like try 'Caesar Cipher' again? (yes/no)").lower()
    if answer == "no":
        should_continue = False
        print("Goodbye!")  