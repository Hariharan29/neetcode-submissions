class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:
        r = len(ob)
        c = len(ob[0])
        dp =[[0]*(c+1) for _ in range(r+1)]
        dp[r-1][c-1]=1 if ob[r-1][c-1]==0 else 0

        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):

                if ob[i][j] == 1:
                    dp[i][j]=0
                elif i==r-1 and j==c-1:
                    continue
            
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]

        return dp[0][0]
  
        