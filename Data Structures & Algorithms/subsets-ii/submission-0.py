class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        s=[]
        nums.sort()

        def dup(i):
            if i==len(nums):
                res.append(s[:])
                return 
            
            s.append(nums[i])
            dup(i+1)

            s.remove(nums[i])
            while i+1 <len(nums) and nums[i]==nums[i+1]:
                i+=1
            dup(i+1)
        dup(0)
        return res
            
        