class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def backtrack(op,cl):
            if op==cl==n:
                res.append("".join(s))
                return
            
            if op<n:
                s.append("(")
                backtrack(op+1,cl)
                s.pop()
            
            if cl<op:
                s.append(")")
                backtrack(op,cl+1)
                s.pop()
        backtrack(0,0)
        return res

        