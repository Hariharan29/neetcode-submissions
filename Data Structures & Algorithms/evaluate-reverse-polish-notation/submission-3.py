class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i in {'+','-','*','/'}:
                t1=s.pop()
                t2=s.pop()
            if i=='+':
                
                s.append(int(t2+t1))
            elif i=='-':
                
                s.append(int(t2-t1))
            elif i=='*':
                
                s.append(t2*t1)
            elif i=='/':
                s.append(int(t2/t1))
            else:
                s.append(int(i))
        return s[0]
        