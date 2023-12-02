import random

rock = ("rock")
paper = ("paper")
sci = ("scissor")

ch = [rock,paper,sci]

print(ch)
us = int(input("choose 0 1 2 "))

if(us > 2 or us < 0):
  print("invalid")

else:
  print("you choose: ")
  print(ch[us])
  co = random.randint(0,2)
  print(ch[co])
  