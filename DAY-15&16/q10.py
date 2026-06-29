#Group Anagrams (LeetCode 49)

def group_anagrams(words):
    from collections import defaultdict
    groups = defaultdict(list)
    
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
        
    return list(groups.values())

words = ['eat','tea','tan','ate','nat','bat']
print(group_anagrams(words))