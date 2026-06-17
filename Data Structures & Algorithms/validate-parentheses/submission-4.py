class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        count=0
        for i in s:
            if i in "({[" :
                sk.append(i)
            elif i==")": 
                if not sk or sk[-1]!="(":
                    return False
                sk.pop()
            elif i=="}":
                if not sk or sk[-1]!="{":
                    return False
                sk.pop()
            elif i=="]":
                if not sk or sk[-1]!="[":
                    return False
                sk.pop()
        return len(sk)==0
            
        
        
            
