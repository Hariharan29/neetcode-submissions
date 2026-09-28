class Solution:
    def ispal(self,s):
            l=0
            r = len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        st= []
        
        def bt(i):
            if i==len(s):
                res.append(st[:])
                return 
            
            for a in range(i,len(s)):
                substr=s[i:a+1]
                if self.ispal(substr):
                    st.append(substr)
                    bt(a+1)
                    st.pop()            
        bt(0)
        return res
        