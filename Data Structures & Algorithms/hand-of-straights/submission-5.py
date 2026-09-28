class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize!=0:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1+ count.get(0,n)
        
        minheap=list(count.keys())

        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if count[i]!=minheap[0]:
                        return False
            return True
                
        