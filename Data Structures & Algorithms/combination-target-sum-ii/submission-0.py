class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        candidates.sort()
        def sum(i,curr):
            if curr==target:
                res.append(subset[:])
                return
            if i>=len(candidates) or curr>target:
                return 
            subset.append(candidates[i])
            sum(i+1,curr+candidates[i])
            subset.pop()
            while i+1 <len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            sum(i+1,curr)

        sum(0,0)
        return res