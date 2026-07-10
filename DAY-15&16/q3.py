#DFS Implementations (Iterative & Recursive)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            print(f'DFS visiting: {node}')
            
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)
                    
    return result


def dfs_recursive(graph, node, visited=None, result=None):
    if visited is None: visited = set()
    if result  is None: result  = []
    
    visited.add(node)
    result.append(node)
    print(f'DFS visiting: {node}')
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, result)
            
    return result

graph = {0:[1,2], 1:[0,3,4], 2:[0,5], 3:[1], 4:[1], 5:[2]}

print('Iterative DFS:', dfs_iterative(graph, 0))
print('Recursive DFS:', dfs_recursive(graph, 0))