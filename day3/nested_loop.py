print("Welcome to the rollercoaster")
height = int(input("what is your height: "))
if height >= 120:
    print("you can ride")
    age = int(input("what is your age: "))
    if age <=18:
      print("pay $7")
    else:
      print("pay $12")
else:
  print("you cant ride")