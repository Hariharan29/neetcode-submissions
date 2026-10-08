class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        dp = [[0 for r  in range(len(nums))] for l in range(len(nums))]
        for l in range(len(nums)-2,0,-1):
            for r in range(1,len(nums)-1):
                if l<=r:
                    dp[l][r] = max(nums[l-1]*nums[i]*nums[r+1]+dp[l][i-1]+dp[i+1][r] for i in range(l,r+1))
        return  max(y[-2] for y in dp)