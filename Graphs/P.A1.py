# Write a function, hasPath, that takes in an object representing the adjacency list of 
# a directed acyclic graph and two nodes (src, dst). The function should return a boolean 
# indicating whether or not there exists a directed path between the source and destination nodes.

# DFS
def hasPath_DFS(graph, src, dst):
    if src == dst:
        return True
    
    for neighbour in graph[src]:
        if hasPath_DFS(graph, neighbour, dst):
            return True
        
    return False

# BFS
from collections import deque
def hasPath_BFS(graph, src, dst):
    q = deque()
    q.append(src)

    while q:
        current_node = q.popleft()
        if current_node == dst: return True
        else: 
            for neighbour in graph[current_node]:
                q.append(neighbour)
    
    return False

