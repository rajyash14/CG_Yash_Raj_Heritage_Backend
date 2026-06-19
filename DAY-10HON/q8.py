a = int(input("Rows: "))

for b in range(a, 0, -1):
    c = ""
    for d in range(b):
        c = c + "*"
    print(c)