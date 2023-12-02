# tip calculator
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("how many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
bill_per_person = bill_with_tip / people
print(f"Each person will pay ${bill_per_person}")