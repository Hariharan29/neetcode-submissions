class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hmap = {i:[] for i in range(n)}
        visit = set()

        for i,j in edges:
            hmap[i].append(j)
            hmap[j].append(i)

        def dfs(n,prev):
            visit.add(n)
            for nei in hmap[n]:
                if nei==prev:
                    continue
                if nei in visit:
                    return False
                if not dfs(nei,n):
                    return False
            return True
        if not dfs(0,-1): 
            return False

        return True if len(visit)==n else False
            
       