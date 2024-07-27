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

# Write your code below this line 👇
choices = [rock, paper, scissors]

print("Select 0 for Rock, 1 for Paper, 2 for Scissors")
user_choice = int(input())
if user_choice not in [0, 1, 2]:
    print("Invalid choice. Please select 0, 1, or 2.")
else:
    print(f"You selected:\n{choices[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer selected:\n{choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins")
