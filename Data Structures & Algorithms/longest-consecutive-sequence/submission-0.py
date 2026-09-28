class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)
        for i in nums:
            for j in range(len(nums)):
                if j-i == 1:
                    cnt[i]=1
        return len(cnt)
        

        