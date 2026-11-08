class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def check(s,l,r):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        while l<r:
            if s[l]!=s[r]:
                return check(s,l+1,r) or check(s,l,r-1)
            l+=1
            r-=1
        return True
        