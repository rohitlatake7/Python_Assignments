# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


k = name1 + name2
lower = k.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

tptal_true = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

lvtotl = l + o + v + e

k = str(tptal_true) + str(lvtotl)
# print(tlv)
tlv = int(k)

if (tlv > 10) and (tlv > 90):
    print(f"Your score is {tlv}, you go together like coke and mentos.")
elif (tlv >= 40) and (tlv <=50):
    print(f"Your score is {tlv}, you are alright  together")
else:
    print(f"Your score is {tlv}")