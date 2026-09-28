class Solution:
    def canFinish(self, numc: int, prer: List[List[int]]) -> bool:
        #phase 1 initialising the adj matrix indegree
        pmap = {i:[] for i in range(numc)}
        indegree=[0]*numc
        for c,p in prer:
            indegree[c]+=1
            pmap[p].append(c)
        #phase 2 adding all the courses with 0 prereq to the queue
        q=deque()
        for n in range(numc):
            if indegree[n]==0:
                q.append(n)

        #phase 3 decre indegree and adding neighbors of elements in queue

        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            for nei in pmap[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return finish == numc
                
        



        