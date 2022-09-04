rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


moves=[rock,paper,scissors]

your_move=int(input('What\'s your move? Choose 0 for rock, 1 for paper or 2 for scissors.'))

if your_move>=3 or your_move<0:
  print('Invalid choice. You lose!')
else:
  print(f'Your move is {moves[your_move]}')
  import random
  comp_move=random.randint(0,2)
  print(f'Computers move: {moves[comp_move]}')
  if your_move==0 and comp_move==2:
    print('You win')
  elif comp_move>your_move:
    print('You lose')
  elif comp_move<your_move:
    print('You win')
  else:
    print('It\'s a tie')
  
