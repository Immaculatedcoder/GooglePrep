# Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
# The function should return the size of the largest connected component in the graph.

from collections import deque
from collections import defaultdict
def largest_component(graph):
    max_count = 0

    seen = set()

    for node in graph:
        if node in seen:
            continue

        # Traverse all node
        def dfs(node):
            count_node = 0
            stk = [node]
            seen.add(node)

            while stk:
                current_node = stk.pop()
                count_node +=1

                for nei_node in graph[current_node]:
                    if nei_node not in seen:
                        seen.add(nei_node)
                        stk.append(nei_node)
                        
            return count_node
        
        max_count = max(max_count, dfs(node))
    return max_count


print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}))



