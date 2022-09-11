from hangman_words import word_list
from hangman_art import logo, stages
import random

print(logo)
chosen_word = random.choice(word_list)
lives=6
display=[]
end_of_game=False

for letter in chosen_word:
  display+=('_')

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter == guess:
      display[position]=guess
  print(f"{''.join(display)}")
  if guess not in chosen_word:
      print(f"{guess} is a wrong guess. You lose a life.")
      lives-=1
      print(stages[lives])
      print(f"You have {lives} lives left.")
      if lives==0:
        print('You lose')
        end_of_game=True
  if '_' not in display:
    end_of_game=True
    print('You win')
