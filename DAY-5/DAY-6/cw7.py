
a = input("Enter password: ")
b = len(a) >= 8
c = False
for d in a:
    if d.isdigit():
        c = True
if b and c:
    print("Strong Password")
else:
    print("Weak Password")