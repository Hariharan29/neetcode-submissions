class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix),len(matrix[0])
        t,b=0,row-1 
        while t <= b:
            r= (t+b)//2
            if target>matrix[r][-1]:
                t=r+1
            elif target<matrix[r][0]:   
                b=r-1
            else:
                break
        if not (t<=b):
            return False
        row=(t+b)//2
        l,r=0,col-1
        while l<=r:
            m=(l+r)//2  
            if target>matrix[row][m]:
                l=m+1
            elif target<matrix[row][m]:   
                r=m-1
            else:
                return True
        return False 
        