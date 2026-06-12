a = 5000  
b = int(input("Enter withdrawal amount: "))

if b <= a:
    if b > 0 and b % 100 == 0:
        print("Withdrawal successful!")
    else:
        print("Amount must be a multiple of 100.")
else:
    print("Insufficient balance!")