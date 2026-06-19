a = int(input("How many numbers? "))
b = []

for c in range(a):
    d = int(input("Enter number: "))
    b.append(d)

e = b[0]
f = b[0]
g = 0
h = 0

for i in b:
    if i > e:
        e = i
    if i < f:
        f = i
    g = g + i
    h = h + 1

print(e)
print(f)
print(g)
print(g / h)