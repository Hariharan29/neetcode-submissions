class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n =len(hand)

            
        if n%groupSize==0:
            return True
        else:
            return False
        