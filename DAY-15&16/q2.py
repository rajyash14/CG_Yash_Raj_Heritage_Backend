#Shortest Path (Unweighted Graph)

from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
        
    visited = {start}
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                new_path = path + [neighbour]
                if neighbour == end:
                    return new_path
                visited.add(neighbour)
                queue.append(new_path)
                
    return None

social_net = {
    'Alice':   ['Bob', 'Carol'],
    'Bob':     ['Alice', 'David'],
    'Carol':   ['Alice', 'Eve'],
    'David':   ['Bob', 'Frank'],
    'Eve':     ['Carol', 'Frank'],
    'Frank':   ['David', 'Eve']
}

path = bfs_shortest_path(social_net, 'Alice', 'Frank')
print(path)