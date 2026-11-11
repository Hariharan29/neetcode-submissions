class NumArray:

    def __init__(self, nums: List[int]):
        self.num = []
        cur = 0
        for n in nums:
            cur+=n
            self.num.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.num[right]
        if left>0:
            leftsum = self.num[left-1]
        else:
            leftsum = 0
        return rightsum-leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)