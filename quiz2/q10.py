a = int(input("Enter marks: "))
b = int(input("Enter family income: "))

if a >= 80:
    if b < 50000:
        print("Eligible for full scholarship!")
    else:
        print("Eligible for partial scholarship!")
else:
    print("Not eligible for scholarship.")