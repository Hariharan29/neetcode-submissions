class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        par = [i for i in range(len(points))]
        rank = [float('inf')]*(len(points))
        edges= []
        def find(n):
            if n!=par[n]:
                par[n]=find(par[n])
            return par[n]
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return True
            
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]

            
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
                edges.append((dist,i,j))
        edges.sort(key = lambda i:i[0])

        for dist,i,j in edges:
            if not union(i,j):
                res+=dist
        return res
        