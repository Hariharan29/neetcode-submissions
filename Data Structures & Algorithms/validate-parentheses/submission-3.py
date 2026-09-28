class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        count=0
        for i in s:
            if i=="(" or "{" or "[" :
                count+=1
                sk.append(i)
            if i==")" and sk[-1]=="(":
                sk.pop()
                sk.pop()
            elif i=="}" and sk[-1]=="{":
                sk.pop()
                sk.pop()
            elif i=="]" and sk[-1]=="[":
                sk.pop()
                sk.pop()
            
        
        if not sk:
            return False
        else:
            return True
            
