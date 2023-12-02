import random

# Rock
rock = """
    _______
---'   ____) 
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
"""
game_img = [rock, paper, scissors]

print("What do you choose?")
user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for scissors.\n "))

if user_choice >=3 or user_choice < 0:
    print("You typed invalid number.You lose!")

else:
  
  print(game_img[user_choice])
  computer_choice = random.randint(0,2)
  
  print("computer chose: ")
  print(game_img[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
  
  elif computer_choice > user_choice:
    print("You Lose!")

  elif(computer_choice < user_choice):
      print("You win")
  
  elif(computer_choice == user_choice):
      print("Draw")

    
  







