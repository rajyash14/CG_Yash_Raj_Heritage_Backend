a = input("Enter text: ").lower()
b = 0
c = 0

for d in a:
    if d in "aeiou":
        b = b + 1
    elif d >= "a" and d <= "z":
        c = c + 1

print(b)
print(c)