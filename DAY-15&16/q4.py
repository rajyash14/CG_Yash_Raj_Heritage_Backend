#Detecting Cycles

def has_cycle_undirected(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True
        return False
        
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

g_cycle = {0:[1,2], 1:[0,2], 2:[0,1]}
g_no_cycle = {0:[1], 1:[0,2], 2:[1]}

print(has_cycle_undirected(g_cycle))
print(has_cycle_undirected(g_no_cycle))