class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [ -x for x in stones]
        heapq.heapify(maxheap)
        
        while len(maxheap)>1:
            y = heapq.heappop(maxheap) 
            x = heapq.heappop(maxheap) 

            if x>y:
                heapq.heappush(maxheap, y-x)
        maxheap.append(0)
        return abs(maxheap[0])
