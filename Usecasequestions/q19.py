def shortest_path(graph, start, end):
    visited = []
    queue = [[start]]
    visited.append(start)
    
    if start == end:
        return [start]
        
    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                
                if neighbor == end:
                    return new_path
                    
                visited.append(neighbor)
                queue.append(new_path)
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

print(shortest_path(graph, 'A', 'E'))