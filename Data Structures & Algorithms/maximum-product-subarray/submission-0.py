class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cinmax,cinmin = 1,1

        for n in range(nums):
            tmp = cinmax*n
            cinmax = max(cinmax*n,cinmin*n,n)
            cinmax = max(cinmax*n,cinmin*n,n)

            res = max(res,cinmax)
        return res
        