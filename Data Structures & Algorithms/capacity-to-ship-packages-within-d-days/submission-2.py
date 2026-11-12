class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res =r

        def canship(m):
            ship=1
            currcap=m
            for w in weights:
                if currcap-w<0:
                    ship+=1
                    currcap=m
                currcap-=w
            return ship<=days
        while l<=r:
            m= (l+r)//2
            if canship(m):
                res = min(res,m)
                r=m-1
            else:
                l=m+1
        return res
        