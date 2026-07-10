def optimized_bubble_sort(marks):
    n = len(marks)
    iterations = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            iterations += 1
            if marks[j] > marks[j + 1]:
                temp = marks[j]
                marks[j] = marks[j + 1]
                marks[j + 1] = temp
                swapped = True
                
        if swapped == False:
            break
            
    print("Loops run:", iterations)
    return marks

marks = [76, 78, 85, 88, 90, 92]
print(optimized_bubble_sort(marks))