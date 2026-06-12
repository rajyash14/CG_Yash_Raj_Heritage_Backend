# Skip Even Numbers (Print Only Odds)

print('Odd numbers from 1 to 20:')
for num in range(1, 21):
        if num % 2 == 0:  
            continue 
        print(num, end=' ')
print()
