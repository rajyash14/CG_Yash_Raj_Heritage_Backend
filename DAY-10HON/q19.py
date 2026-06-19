a = {}

while True:
    b = input("1:Mark 2:View 3:Search 4:Exit -> ")
    
    if b == "1":
        c = input("Name: ")
        d = int(input("Percent: "))
        a[c] = d
    elif b == "2":
        for c in a:
            print(c, a[c])
        print("<75%:")
        for c in a:
            if a[c] < 75:
                print(c)
    elif b == "3":
        c = input("Name: ")
        if c in a:
            print(a[c])
        else:
            print("Not found")
    elif b == "4":
        break