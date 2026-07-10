def average_temperature(temps, k=7):
    if len(temps) < k:
        return []
        
    window_sum = 0
    averages = []
    
    for i in range(k):
        window_sum += temps[i]
        
    averages.append(window_sum / k)
    
    for i in range(k, len(temps)):
        window_sum = window_sum - temps[i - k] + temps[i]
        averages.append(window_sum / k)
        
    return averages

temperatures = [30, 32, 31, 29, 28, 33, 35, 34, 31, 30]
print(average_temperature(temperatures, 7))