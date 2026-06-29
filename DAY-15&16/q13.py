#Valid Anagram (LeetCode 242)

from collections import Counter

def is_valid_anagram(s, t):
    return Counter(s) == Counter(t)

print(is_valid_anagram('anagram', 'nagaram'))
print(is_valid_anagram('rat', 'car'))