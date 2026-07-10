p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in years: "))

a = p * ((1 + r / 100) ** t)
interest = a - p

print("Final Amount:", round(a, 2))
print("Interest Earned:", round(interest, 2))