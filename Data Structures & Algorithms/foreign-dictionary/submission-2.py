class Solution:
    def foreignDictionary(self, word: List[str]) -> str:
        adj = {c:set() for w in word for c in w}

        for i in range(len(word)-1):
            w1,w2 = word[i],word[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res= []
        #default DFS template for Topological sort
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c]=True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c]=False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        
        return "".join(res)
             

        
