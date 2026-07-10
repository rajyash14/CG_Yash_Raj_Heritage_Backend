def longest_substring(s):
    seen = []
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        seen.append(s[right])
        
        if len(seen) > max_length:
            max_length = len(seen)
            
    return max_length

text = "abcabcbb"
print(longest_substring(text))