#Longest Substring Without Repeating Characters (LeetCode 3)

def length_of_longest_substring(s):
    char_set = set()
    left     = 0
    max_len  = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len

def longest_substring_optimized(s):
    last_seen = {}
    left      = 0
    max_len   = 0
    
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
            
        last_seen[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

print(length_of_longest_substring('abcabcbb'))
print(longest_substring_optimized('tmmzuxt'))