class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        taken = [False]*len(nums)
        ds=[]
        def perm(ds,taken):
            if len(ds)==len(nums):
                res.append(ds[:])
                return
            for i in range(len(nums)):
                if not taken[i]:
                    ds.append(nums[i])
                    taken[i]=True
                    perm(nums,ds,taken,res)
                    ds.pop()
                    taken[i]=False

        perm(ds,taken)
        return res
                
        