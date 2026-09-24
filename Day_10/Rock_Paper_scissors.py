import random

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
game_variables = [rock, paper, scissors]
input_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if input_choice >=3:
    raise ValueError("You typed an invalid number, you lose!")
if input_choice == 0:
    print(rock)
elif input_choice == 1:
    print(paper)
else:
    print(scissors)

random_choice = random.randint(0, 2)

if random_choice == 0:
    print("Computer chose:")
    print(rock)
elif random_choice == 1:
    print("Computer chose:")
    print(paper)
else:
    print("Computer chose:")
    print(scissors)

if input_choice == 0 and random_choice == 2:
    print("You win!")
elif input_choice == 2 and random_choice == 1:
    print("You win!")
elif input_choice == 1 and random_choice == 0:
    print("You win!")
elif input_choice == 2 and random_choice == 0:
    print("You lose!")
elif input_choice == 1 and random_choice == 2:
    print("You lose!")
elif input_choice == 0 and random_choice == 1:
    print("You lose!")
elif input_choice == random_choice:
    print("It's a draw!")
