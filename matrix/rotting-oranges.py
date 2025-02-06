class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        new_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while fresh:
            if not rotten:
                return -1
            
            new_rotten = set()
            for i, j in rotten:
                for di, dj in new_dir:
                    ni, nj = i + di, j + dj
                    if (ni, nj) in fresh:
                        new_rotten.add((ni, nj))
        
        fresh -= new_rotten
        rotten = new_rotten
        timer += 1

        return timer

        # Time O(m*n) where m, n are the number of rows and col
        # Space O(m*n) in worst case, when all org are fresh