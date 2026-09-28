class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0,0,0]

        for t in triplets:
            if t[0]>target[0] or t[1]> target[1] or t[2]> target[2]:
                continue
            cur[0]=max(cur[0],t[0])
            cur[1]=max(cur[1],t[1])
            cur[2]=max(cur[2],t[2])
        return cur==target
        