# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return the length of the shortest path between A and B. Consider the length as the number of edges
#  in the path, not the number of nodes. If there is no path between A and B, then return -1. 
# You can assume that A and B exist as nodes in the graph.

from collections import deque
from collections import defaultdict

def shortest_path(edges, node_A, node_B):
    if node_A == node_B:
        return 0
    

    # Convert to adjacency list for Graph Traversal
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    def bfs(start):
        q = deque()
        q.append((start, 0))
        seen.add(start)

        while q:
            current_node = q.popleft()
            if current_node[0] == node_B:
                return current_node[1]
                
            
            for nei_node in graph[current_node[0]]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append((nei_node, current_node[1] + 1))
        return -1
    
    min_edge_count = bfs(node_A)
    
    return min_edge_count

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))
