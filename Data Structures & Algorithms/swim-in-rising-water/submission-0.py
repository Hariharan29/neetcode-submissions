class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [(grid[0][0],0,0)]
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        while minheap:
            w1,r1,c1 = heapq.heappop(minheap)
            if (r1,c1) in visit:
                continue
            elif (r1,c1)==(rows-1,cols-1):
                return w1
            visit.add((r1,c1))

            for dr, dc in directions:
                nr,nc  = dr + r1 , dc+c1

                if 0<=nr<rows and 0<=nc<cols:
                    if (nr,nc) not in visit:
                        res = max(w1,grid[nr][nc])
                        heapq.heappush(minheap,(res,nr,nc))
            
