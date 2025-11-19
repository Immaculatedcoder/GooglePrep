# Write a function, minimum_island, that takes in a grid containing Ws and Ls. 
# W represents water and L represents land. The function should return the size of the smallest island. 
# An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

# '1' -> 'L'
# '0' -> 'W'

from collections import defaultdict

def minimum_island(grid):
    # Convert the grid to Adjaceny list of its neighbours
    graph = defaultdict(list)
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                graph[(r,c)]

                if r > 0 and grid[r-1][c] == '1':
                    graph[(r,c)].append((r-1,c))
                if r < rows - 1 and grid[r+1][c] == '1':
                    graph[(r,c)].append((r+1,c))
                if c > 0 and grid[r][c-1] == '1':
                    graph[(r,c)].append((r,c-1))
                if c < cols - 1 and grid[r][c+1] == '1':
                    graph[(r,c)].append((r,c+1))

    seen = set()
    def dfs(start):
        count_node = 0
        stk = [start]
        seen.add(start)
        
        while stk:
            current_node = stk.pop()
            count_node += 1

            for nei_node in graph[current_node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stk.append(nei_node)

        return count_node
    
    min_count = float('inf')

    for node in graph:
        if node in seen:
            continue

        min_count = min(min_count, dfs(node))

    return min_count



