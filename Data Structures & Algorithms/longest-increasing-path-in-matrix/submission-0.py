class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        

        def dfs(i,j):
            if dp[i][j]!=0:
                return dp[i][j]
            longest = 1
            if i>0 and matrix[i-1][j]>matrix[i][j]:
                longest = max(longest,1+dfs(i-1,j))
            if i<r-1 and matrix[i+1][j]>matrix[i][j]:
                longest = max(longest,1+dfs(i+1,j))
            if j>0 and matrix[i][j-1]>matrix[i][j]:
                longest = max(longest,1+dfs(i,j-1))
            if j<c-1 and matrix[i][j+1]>matrix[i][j]:
                longest = max(longest,1+dfs(i,j+1))
            dp[i][j] = longest
            return longest
        r = len(matrix)
        c = len(matrix[0])

        dp = [[0]*(c) for _ in range(r)]
        answer = 0 
        for i in range(r):
            for j in range(c):
                answer = max(answer,dfs(i,j))
        return answer
        