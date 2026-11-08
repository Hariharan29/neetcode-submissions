class Solution:
    def rotate(self, s: List[int], k: int) -> None:
        n=len(s)
        k %=n
        l=0
        r=len(s)-1
        def reverse(l,r):
            while l<r:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        return s
        