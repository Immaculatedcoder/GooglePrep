# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
# The function should return the number of connected components within the graph.

from collections import deque
def connected_components_count(graph):
    count = 0

    seen = set()
    for node in graph:
        if node in seen:
            continue

        # DFS
        def dfs(node):
            stk = [node]
            seen.add(node)

            while stk:
                current_node = stk.pop()
                for nei_node in graph[current_node]:
                    if nei_node not in seen:
                        seen.add(nei_node)
                        stk.append(nei_node)
        
        count += 1

        dfs(node)
    return count

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})