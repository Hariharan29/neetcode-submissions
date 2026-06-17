class Solution(object):
    def twoSum(self, nums, target):
        m={}

        for i,n in enumerate(nums):
            Diff=target-n
            if Diff in m:
                return [m[Diff],i]
            m[n]=i