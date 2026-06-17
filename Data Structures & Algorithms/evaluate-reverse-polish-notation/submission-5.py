class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i=='+':
                t1=s.pop()
                t2=s.pop()
                s.append(int(t2+t1))
            elif i=='-':
                t1=s.pop()
                t2=s.pop()
                s.append(int(t2-t1))
            elif i=='*':
                t1=s.pop()
                t2=s.pop()
                s.append(t2*t1)
            elif i=='/':
                t1=s.pop()
                t2=s.pop()
                s.append(int(float(t2)/t1))
            else:
                s.append(int(i))
        return s[0]
        