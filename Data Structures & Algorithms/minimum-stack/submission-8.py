class MinStack:

    def __init__(self):
        self.sk=[]
        

    def push(self, val: int) -> None:
        self.sk.append(val)
        

    def pop(self) -> None:
        if self.sk:
            self.sk.pop()
        

    def top(self) -> int:
        if not self.sk:
            return None
        else:
            return self.sk[-1]
        

    def getMin(self) -> int:
        if not self.sk:
            return None
        return min(self.sk)
        
