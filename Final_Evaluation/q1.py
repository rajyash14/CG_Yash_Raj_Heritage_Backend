def q1():
    try:
        a = float(input("Enter weight in kg: "))
        b = float(input("Enter height in centimeters (e.g., 175): "))
        
        b = b / 100
            
        c = a / (b ** 2)
        
        if c < 18.5:
            d = "Underweight"
        elif c < 25:
            d = "Normal"
        elif c < 30:
            d = "Overweight"
        else:
            d = "Obese"
            
        print(f"BMI: {c:.2f}, Category: {d}")
        
        e = int(input("Enter birth year: "))
        f = 2026 - e
        print(f"Current age: {f}")
    except ValueError:
        print("Invalid input")

q1()