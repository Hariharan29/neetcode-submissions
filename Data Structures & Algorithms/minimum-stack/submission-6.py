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
        return min(self.sk)
        
