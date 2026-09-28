class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s= 0
        m = nums[0]
        for i in range(len(nums)):
            s+=nums[i]
            m = max(m,s)

            if s<0:
                s=0
        return m
        