class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]]
        res =0

        for start,end in intervals[1:]:
            if start < output[-1][1]:
                res+=1
            else:
                output.append([start,end])
        return res
        