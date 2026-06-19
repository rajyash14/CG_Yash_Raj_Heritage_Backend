a = int(input("Rows: "))

for b in range(1, a + 1):
    c = ""
    for d in range(b):
        c = c + "*"
    print(c)