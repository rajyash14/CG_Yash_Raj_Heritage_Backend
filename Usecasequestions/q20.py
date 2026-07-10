def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited_nodes = []
dfs_recursive(graph, 'A', visited_nodes)