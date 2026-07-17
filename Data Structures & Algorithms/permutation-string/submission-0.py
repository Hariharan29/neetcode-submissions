class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0

        char1={}
        char2={}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            char1[s1[i]]=1+char1.get(s1[i],0)
        
        for r in range(len(s2)):
            char2[s2[r]]=1+char2.get(s2[r],0)
            if (r-l+1)>len(s1):
                char2[s2[l]]-=1
                if char2[s2[l]]==0:
                    del char2[s2[l]]
                l+=1
            if char1==char2:
                return True
            
        return False
        