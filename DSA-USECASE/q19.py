def selection_sort_rank(scores):
    n = len(scores)
    
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if scores[j] > scores[max_index]:
                max_index = j
                
        temp = scores[i]
        scores[i] = scores[max_index]
        scores[max_index] = temp
        
    return scores

players = [500, 1200, 800, 300, 1500]
print(selection_sort_rank(players))