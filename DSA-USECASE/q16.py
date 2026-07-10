def detect_failed_logins(logs, k):
    failed_count = 0
    
    for i in range(k):
        if logs[i] == "Failed":
            failed_count += 1
            
    if failed_count == k:
        return True
        
    for i in range(k, len(logs)):
        if logs[i - k] == "Failed":
            failed_count -= 1
        if logs[i] == "Failed":
            failed_count += 1
            
        if failed_count == k:
            return True
            
    return False

network_logs = ["Success", "Failed", "Failed", "Failed", "Success"]
k = 3
print(detect_failed_logins(network_logs, k))