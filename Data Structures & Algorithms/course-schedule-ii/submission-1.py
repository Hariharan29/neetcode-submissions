class Solution:
    def findOrder(self, numc: int, prer: List[List[int]]) -> List[int]:
        pmap = {i:[] for i in range(numc)}
        indegree = [0]*numc

        for c,p in prer:
            indegree[c]+=1
            pmap[p].append(c)

        q=deque()
        for n in range(numc):
            if indegree[n]==0:
                q.append(n)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in pmap[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return topo if len(topo)==numc else []