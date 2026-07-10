def min_difference_pair(heights):
    if len(heights) < 2:
        return []
        
    left = 0
    right = 1
    min_diff = float('inf')
    best_pair = []
    
    while right < len(heights):
        diff = heights[right] - heights[left]
        
        if diff < min_diff:
            min_diff = diff
            best_pair = [heights[left], heights[right]]
            
        left += 1
        right += 1
        
    return best_pair

heights = [150, 152, 159, 160, 165, 170]
print(min_difference_pair(heights))