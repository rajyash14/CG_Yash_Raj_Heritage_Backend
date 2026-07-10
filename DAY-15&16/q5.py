#Social Network Analysis

def connections_within_degrees(graph, start, max_degrees):
    from collections import deque
    
    visited = {start: 0}
    queue = deque([(start, 0)])
    connections = {1: [], 2: [], 3: []}
    
    while queue:
        person, degree = queue.popleft()
        
        for friend in graph.get(person, []):
            if friend not in visited and degree + 1 <= max_degrees:
                visited[friend] = degree + 1
                connections[degree+1].append(friend)
                queue.append((friend, degree + 1))
                
    return connections

linkedin = {
    'Alice':   ['Bob', 'Carol'],
    'Bob':     ['Alice', 'David', 'Eve'],
    'Carol':   ['Alice', 'Frank'],
    'David':   ['Bob'],
    'Eve':     ['Bob', 'Grace'],
    'Frank':   ['Carol'],
    'Grace':   ['Eve']
}

result = connections_within_degrees(linkedin, 'Alice', 3)
print('1st degree:', result[1])
print('2nd degree:', result[2])
print('3rd degree:', result[3])