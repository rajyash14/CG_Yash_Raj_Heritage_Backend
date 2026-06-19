a = int(input("How many items? "))
b = []

for c in range(a):
    d = input("Enter item: ")
    b.append(d)

e = []

for f in b:
    if f not in e:
        e.append(f)

print(e)