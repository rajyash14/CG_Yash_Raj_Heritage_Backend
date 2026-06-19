a = int(input("Enter max table number: "))

for b in range(1, a + 1):
    for c in range(1, 21):
        print(b, "x", c, "=", b * c)
    print("---")
    