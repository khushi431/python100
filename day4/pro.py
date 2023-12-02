import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
""")


game_imgs = [rock, paper, scissors]

print("What do you choose?")
users_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors.\n"))

if users_choice >= 3 or users_choice < 0: 
  print("You typed an invalid number. You lose!")
  
else:
  print("\nYou Choose: ")
  print(game_imgs[users_choice])
  
  computers_choice = random.randint(0,2)
  
  print("Computer chose:")
  print(game_imgs[computers_choice])
  
  if (users_choice == 0 and computers_choice == 2):
    print("You win!")
  
  elif (computers_choice == 0 and users_choice == 2):
    print("You lose!")
  
  elif (computers_choice > users_choice):
    print("You Lose!")
  
  elif (users_choice > computers_choice):
    print("You win!")
  
  elif (computers_choice == users_choice):
    print("It's a tie!")

  
      