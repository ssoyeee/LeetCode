class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: #empty
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0 #number of islands

        def bfs(r,c):
            q = collections.deque() #normally used for bfs
            visited.add((r,c)) #must be tuple format
            q.append((r,c))

            while q: #expanding our island
                row, col = q.popleft() #pop from the queue-bfs
                directions = [[1,0],[-1,0],[0,1],[0,-1]] #4 directions that we can go with 

                for dr,dc in directions: #check this position is inbound
                    r,c = row+dr, col+dc #compute our new rows, cols coordinate based on the direction that we're at 
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and #it's land
                       (r, c) not in visited): #it hasn't been visited
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited: 
                    bfs(r,c)
                    islands += 1
        return islands
