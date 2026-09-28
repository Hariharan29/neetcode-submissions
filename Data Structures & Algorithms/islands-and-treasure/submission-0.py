class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid),len(grid[0])
        visit = set()
        q = deque()

        def addr(r,c):
            if (r==ROWS or c==COLS or min(r,c)<0 or grid[r][c]==-1 or (r,c) in visit):
                return 
            q.append([r,c])
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0 
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist 
                addr(r+1,c)
                addr(r-1,c)
                addr(r,c+1)
                addr(r,c-1)
            dist+=1
                
