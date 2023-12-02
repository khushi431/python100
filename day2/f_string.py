age = input("enter your age:")
int_age = int(age)
years_remain = 90 - int_age
months_remain = years_remain * 12
weeks_remain = years_remain * 52
days_remain = years_remain * 365
message = f" {days_remain} days, {weeks_remain} weeks, and {months_remain} months."
print(message) 

