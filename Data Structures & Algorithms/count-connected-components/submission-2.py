class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def dfs(k):
            visit.add(k)
            for nei in adj[k]:
                if nei not in visit:
                    dfs(nei)

        res=0
        for n in range(n):
            if n not in visit:
                dfs(n)
                res+=1
            
        return res
        
            

        