def find_unique_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
            
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
                
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return pairs

arr = [1, 2, 2, 3, 4, 5, 5, 6]
target = 7
print(find_unique_pairs(arr, target))