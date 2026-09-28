class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        s=[]
        def sub(i):
            while i>=len(nums):
                res.append(s[:])
                return
            s.append(nums[i])
            sub(i+1)
            s.remove(nums[i])
            sub(i+1)
        sub(0)
        return res
        