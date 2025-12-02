'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

from collections import defaultdict
def exist(board, word):

    graph = defaultdict(list)
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if r > 0:
                graph[(r,c)].append((r-1,c))
            if r < rows - 1:
                graph[(r,c)].append((r+1,c))
            if c > 0:
                graph[(r,c)].append((r,c-1))
            if c < cols - 1:
                graph[(r,c)].append((r,c+1))

    w = len(word)
    visited = set()
    def dfs(r,c,i):
        if board[r][c] != word[i]:
            return False
        if i == w - 1:
            return True
        
        visited.add((r,c))

        for nr, nc in graph[(r,c)]:
            if (nr, nc) not in visited:
                if dfs(nr,nc,i+1):
                    return True
                
        visited.remove((r,c))
        
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(r,c,0):
                    return True
    
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABZ"

print(exist(board, word))
    
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         rows = len(board)
#         cols = len(board[0])
#         visited = set()
        

#         def dfs(r,c,i):
#             if board[r][c] != word[i]:
#                 return False
#             if i == len(word) - 1:
#                 return True

#             visited.add((r,c))
#             for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0)]:
#                 nr, nc = r + dr, c + dc

#                 if 0 <= nr < rows and 0 <= nc < cols:
#                     if (nr, nc) not in visited:
#                         if dfs(nr,nc,i+1):
#                             return True
#             visited.remove((r,c))

#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == word[0]:
#                     if dfs(r,c,0):
#                         return True

#         return False  




    

    