class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        st=0
        fleet=0
        for p,s in pair:
            time=float(target-p)/s
            if time>st:
                fleet+=1
                st=time
        return fleet
