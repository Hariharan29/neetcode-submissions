class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row  = len(grid)
        col =len(grid[0])
        res =0
        count=0

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            count=1
            count+=dfs(r+1,c)
            count+=dfs(r-1,c)
            count+=dfs(r,c+1)
            count+=dfs(r,c-1)
            return count 
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    res = max(res,dfs(r,c))
        return res
        