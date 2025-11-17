# Write a function, undirected_path, that takes in a list of edges for an undirected graph
#  and two nodes (node_A, node_B). The function should return a boolean indicating whether 
# or not there exists a path between node_A and node_B.


from collections import defaultdict
from collections import deque

def undirected_path(edges, node_A, node_B):
    if node_A == node_B:
        return True

    undirected_graph = defaultdict(list)
    for u, v in edges:
        undirected_graph[u].append(v)
        undirected_graph[v].append(u)

    seen = set()
    seen.add(node_A)

    def dfs(node):
        stk = [node]

        while stk:
            current_node = stk.pop()
            if current_node == node_B:
                return True

            for nei_node in undirected_graph[current_node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stk.append(nei_node)
        return False
    
    return dfs(node_A)

