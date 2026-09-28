class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [False,False,False]

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            if t[0]==target[0]:
                ans[0] = True
            if t[1]==target[1]:
                ans[1] = True
            if t[2]==target[2]:
                ans[2] = True
        return ans[0] and ans[1] and ans[2]
        