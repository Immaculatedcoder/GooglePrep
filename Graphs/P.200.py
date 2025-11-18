#  1 - land
#  0 - water
# nodes (row,col)

from collections import defaultdict
from collections import deque

def numIslands(grid):
    seen_Island = 0
    seen = set()

    # Convert grid Adjacency list of nodes
    graph = defaultdict(list)
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                graph[(r,c,grid[r][c])]

                if r > 0 and grid[r-1][c] == '1': 
                    graph[(r,c,grid[r][c])].append((r-1,c,grid[r-1][c]))
                if r < rows - 1 and grid[r+1][c] == '1':
                    graph[(r,c,grid[r][c])].append((r+1,c,grid[r+1][c]))
                if c > 0 and grid[r][c-1] == '1':
                    graph[(r,c,grid[r][c])].append((r, c-1, grid[r][c-1]))
                if c < cols - 1 and grid[r][c+1] == '1':
                    graph[(r, c,grid[r][c])].append((r, c+1,grid[r][c+1]))


    def bfs(start):
        q = deque()
        q.append(start)
        seen.add(start)

        while q:
            current_node = q.popleft()

            for nei_node in graph[current_node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
    
    for node in graph:
        if node in seen:
            continue

        seen_Island += 1
        bfs(node)

    return seen_Island

#####################################
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

output = numIslands(grid)
print(output)