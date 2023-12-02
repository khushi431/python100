import os

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------. 
                      /_______________\\
'''

print (logo)

game_end = False

bids = {}

while not game_end:

  name = input("What is your name?\n")
  bid = int(input("How much are you bidding? $"))

  bids[name] = bid
  game = input("Are there any other bidders. yes or no\n").lower()

  if game == "no":
    game_end = True

highest_bid = 0

for bidder in bids:
  if bid > highest_bid:
    highest_bid = bid
    winner = bidder
print(f"The winner is {bidder} with a bid of ${highest_bid}")
clear()