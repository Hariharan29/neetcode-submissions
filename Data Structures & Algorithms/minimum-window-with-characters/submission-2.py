class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count,window  = {},{}
        l=0
        if len(t)==0: return ""
        res,reslen=[-1,-1], float('infinity')
        
        for i in range(len(t)):
            count[t[i]]=1+count.get(t[i],0)
        have, need = 0,len(count)
        
        for r in range(len(s)):
            window[s[r]]=1+ window.get(s[r],0)
        
            if s[r] in count and count[s[r]]==window[s[r]]:
                have+=1

            while have == need:
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                window[s[l]]-=1
                if s[l] in count and count[s[l]]> window[s[l]]:
                    have-=1
                l+=1
        l,r = res
        if reslen!=float('infinity'):
            return s[l:r+1]
        else:
            return ""
                

    


        