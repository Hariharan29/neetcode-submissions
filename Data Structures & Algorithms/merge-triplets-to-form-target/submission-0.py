class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = []

        for i in triplets:
            res.append([max(triplets[0][0],triplets[1][0]),max(triplets[0][1],triplets[1][1]),max(triplets[0][2],triplets[1][2])])
            if res!=target:
                return False
            return True