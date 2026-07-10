#Frequency Count Pattern

from collections import Counter

def most_frequent(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return max(freq, key=freq.get)

def most_frequent_v2(arr):
    return Counter(arr).most_common(1)[0][0]

print(most_frequent([1,3,2,3,4,3,1]))

web_logs = ['python', 'java', 'python', 'go', 'java', 'python']
keyword_counts = Counter(web_logs)
print(keyword_counts)