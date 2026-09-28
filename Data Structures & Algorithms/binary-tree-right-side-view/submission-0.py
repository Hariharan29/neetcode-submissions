# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q= collections.deque()
        q.append(root)
        res = []
        

        while q:
            lenq= len(q)
            rightmost=None
            for i in range(lenq):
                node = q.popleft()
                if node:
                    rightmost=node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost.val)

        return res

        