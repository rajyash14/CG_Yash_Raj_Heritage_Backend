def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)
    
    while len(queue) > 0:
        node = queue.pop(0)
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')