class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def count(i):
            if i==0 or i==1:
                return 1
            
            if dp[i]!=-1:
                return dp[i]
            dp[i]=count(i-1)+count(i-2)
            return dp[i]
        return count(n)
            