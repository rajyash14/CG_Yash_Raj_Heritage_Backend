a = int(input("Enter secret number: "))

while True:
    b = int(input("Guess: "))
    
    if b == a:
        print("Win!")
        break
    elif b < a:
        print("Low")
    else:
        print("High")