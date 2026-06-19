a = {}

while True:
    b = input("1:Add 2:Search 3:Delete 4:Exit")
    
    if b == "1":
        c = input("Name: ")
        d = input("Salary: ")
        a[c] = d
    elif b == "2":
        c = input("Name: ")
        if c in a:
            print(a[c])
        else:
            print("Not found")
    elif b == "3":
        c = input("Name: ")
        if c in a:
            del a[c]
    elif b == "4":
        break