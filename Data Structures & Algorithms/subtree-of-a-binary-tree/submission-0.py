# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.sametree(root,subRoot):
            return False
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def sametree(self,s,t):
        if not s and not t:
            return True
        if s and t and s.val==t.val:
            return self.sametree(s.left,t) and self.sametree(s.right,t)
        return False