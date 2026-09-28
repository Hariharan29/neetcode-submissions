class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n =len(hand)

            
        if n%3==0:
            return True
        else:
            return False
        