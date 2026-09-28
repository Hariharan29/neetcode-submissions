class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        count=0
        for i in s:
            if i=="(" or "{" or "[" :
                count+=1
                sk.append(i)
            if i==")" or "}" or "]":
                sk.append(i)
                count-=1
                sk.pop()
                sk.pop()
        
        if not sk:
            return True
        else:
            return False
            
