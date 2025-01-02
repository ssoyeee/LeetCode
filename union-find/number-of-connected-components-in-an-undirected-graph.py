class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(index):
            if not visited and graph[index][i]:
                visited[index] = True
                answer += 1
            
       # Input and initialize
        graph = [[False] * (n+1) for _ in range(n+1)]
        visited = [False] * (n+1)
        answer = 0
        
        # fill out connected components
        for u, v in edges:
            graph[u][v] = True
            graph[v][u] = True
        
        # call dfs
        for i in range(1, n+1):
            dfs(i)

        return answer-1