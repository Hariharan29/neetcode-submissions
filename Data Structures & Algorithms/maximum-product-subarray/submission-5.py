class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cinmax,cinmin = 1,1

        for n in nums:
            tmp = cinmax*n
            cinmax = max(n*cinmax,n*cinmin,n)
            cinmax = min(tmp,n*cinmin,n)

            res = max(res,cinmax)
        return res
        