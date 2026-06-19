a = int(input("How many numbers? "))
b = []

for c in range(a):
    d = int(input("Enter number: "))
    b.append(d)

e = -999999999
f = -999999999

for g in b:
    if g > e:
        f = e
        e = g
    elif g > f and g < e:
        f = g

print(f)