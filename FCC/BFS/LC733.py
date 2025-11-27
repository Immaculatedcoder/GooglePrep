'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.


'''
from collections import defaultdict, deque
def floodFill(image,sr, sc, color):

    rows = len(image)
    cols = len(image[0])

    sp = image[sr][sc]
    graphs = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if image[r][c] == sp:
                graphs[(r,c)]

                if r > 0 and image[r-1][c] == sp:
                    graphs[(r,c)].append((r-1,c))
                if r < rows -1 and image[r+1][c] == sp:
                    graphs[(r,c)].append((r+1,c))
                if c > 0 and image[r][c-1] == sp:
                    graphs[(r,c)].append((r,c-1))
                if c < cols -1 and image[r][c+1] == sp:
                    graphs[(r,c)].append((r,c+1))
    
    seen = set()
    def bfs(start,image, color):
        q = deque()
        q.append(start)
        seen.add(start)

        while q:
            current_node = q.popleft()
            r,c = current_node
            image[r][c] = color

            for nei_node in graphs[current_node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
        return image
    start = (sr, sc)
    return bfs(start,image, color)

image = [[0,0,0],[0,0,0]]
sr = 1
sc = 0
color = 2

print(floodFill(image,sc,sr,color))