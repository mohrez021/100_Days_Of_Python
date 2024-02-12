from random import choice
from hangman_art import stages, logo
from hangman_words import word_list 

print(logo)

lives = 6
word_list = word_list
chosen_word = choice(word_list)
word_length = len(chosen_word)
repititive = []
# print(f'the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

guess = ""
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
        
    for index in range(word_length):
      if guess == chosen_word[index]:
         display[index] = guess
    
    if guess in repititive:
        print(f"You've already guessed '{guess}'")
    
    if "_" not in display:
        end_of_game = True
        print("You win")

    if guess not in chosen_word:
        if guess in repititive:
            pass
        else:
            print(f"You guessed '{guess}', that's not in the word. you lose a life.")
            lives -= 1
            repititive.append(guess)

        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The correct answer was {chosen_word}.')


        
    print(' '.join(display))    
    print(stages[lives])
    repititive.append(guess)



