def bubble_sort(marks):
    n = len(marks)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                temp = marks[j]
                marks[j] = marks[j + 1]
                marks[j + 1] = temp
                
    return marks

exam_marks = [85, 92, 78, 90, 88, 76]
print(bubble_sort(exam_marks))