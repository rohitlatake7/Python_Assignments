# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


years = 90 - int(age)
months = int (years) * 12
days = int(years) * 365
# print(days)
weeks = int(years) * 52
# print(weeks)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")