class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(set)
        count=0
        if len(nums)==1:
            return 1
        for i in nums:
            for j in range(len(nums)):
                if j-i == 1:
                    cnt[i]=1
            if i in cnt:
                count+=1
        return count-1
        

        