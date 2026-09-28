class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        minheap = [(0,0)]
        res=0
        visit = set()

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append([dist,j])
            
        while minheap:
            dist,j = heapq.heappop(minheap)
            if j in visit:
                continue 
            visit.add(j)
            res+=dist
            for ndist,n in adj[j]:
                if n not in visit:
                    heapq.heappush(minheap,[ndist,n])

        return res

        
