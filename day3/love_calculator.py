print("Welcome to the love calculator")
name1 = input("Enter your name:")
name2 = input("Enter their name: ")

combined_names = name1 + name2
lower_case_names = combined_names.lower()

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")

true = t + r + u + e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

# print love score
int_love_score = int(love_score)
print(love_score)
if (int_love_score < 10) or (int_love_score > 90):
  print(f"Your Score is {int_love_score}, you go like coke and mentor")

elif (int_love_score >= 40) and (int_love_score <= 50):
  print(f"Your Score is {int_love_score}, you are alright together")

else:
  print(f"your score is {int_love_score} jnjbnk")
