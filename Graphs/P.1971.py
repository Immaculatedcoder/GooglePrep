from collections import defaultdict
from collections import deque
def validPath(n, edges, source, destination):
    if source == destination:
        return True
    
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    seen.add(source)

    # # 1. DFS using Call Stack
    # def dfs(node):
    #     if node == destination:
    #         return True
        
    #     for neighbor in graph[node]:
    #         if neighbor not in seen:
    #             seen.add(neighbor)
    #             if dfs(neighbor):
    #                 return True
    #     return False
    # return dfs(source)

    # # 2. DFS using iterative stack
    # def dfs(node):
    #     stk = [node]

    #     while stk:
    #         current_node = stk.pop()
    #         if current_node == destination:
    #             return True
            
    #         for neighnour in graph[current_node]:
    #             if neighnour not in seen:
    #                 seen.add(neighnour)
    #                 stk.append(neighnour)
    #     return False
    
    # return dfs(source)


    # 3. BFS 
    def bfs(node):        
        q = deque()
        q.append(node)
        
        while q:
            current_node = q.popleft()
            if current_node == destination:
                return True
            
            for neighbour in graph[current_node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)

        return False
    
    return bfs(source)

