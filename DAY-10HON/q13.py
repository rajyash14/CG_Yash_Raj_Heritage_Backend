a = input("Enter a sentence: ")
b = ""
c = []

for d in a:
    if d != " ":
        b = b + d
    else:
        if b != "":
            c.append(b)
            b = ""
if b != "":
    c.append(b)

e = {}

for f in c:
    if f in e:
        e[f] = e[f] + 1
    else:
        e[f] = 1

print(e)