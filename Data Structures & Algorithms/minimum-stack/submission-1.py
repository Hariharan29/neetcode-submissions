class MinStack:

    def __init__(self):
        self.sk=[]
        

    def push(self, val: int) -> None:
        self.sk.append(val)
        

    def pop(self) -> None:
        self.sk.pop()
        

    def top(self) -> int:
        t=self.sk.pop()
        return t
        

    def getMin(self) -> int:
        
        for i in self.sk:
            m=i
            m = min(i,m)
            i+=1
        return m
        
