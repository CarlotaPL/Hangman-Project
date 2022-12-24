import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()

    clear()
  
    if guess in display:
      print("You have already entered this letter.")
      
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess
        
    if guess not in chosen_word:
      print(f"Letter {guess} is not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win.")

    print(stages[lives])
