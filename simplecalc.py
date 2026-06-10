x = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
y = float(input("Second number: "))

if op == '+': print(x + y)
elif op == '-': print(x - y)
elif op == '*': print(x * y)
elif op == '/' and y != 0: print(x / y)
else: print("Error!")