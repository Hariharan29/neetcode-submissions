class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        
        def sum(i,curr):
                if curr==target:
                    res.append(path[:])
                    return
                
                if i>=len(nums) and curr>target:
                    return

                #decision to take
                path.append(nums[i])
                sum(i,curr+nums[i])
                #decision to not take
                path.pop()
                
                sum(i+1,curr)
        sum(0,0)
        return res

        