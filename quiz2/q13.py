a = int(input("Enter your age: "))

if a < 12:
    print("Ticket price is $5 (Child)")
elif a <= 60:
    print("Ticket price is $15 (Adult)")
else:
    print("Ticket price is $10 (Senior)")