# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, p, q):
        dummy=ListNode()
        tail = dummy
        
        while p and q:
            if p.val<=q.val:
                tail.next=p
                p=p.next
            else:
                tail.next=q
                q=q.next
            tail=tail.next
        if p:
            tail.next=p
        elif q:
            tail.next=q
        return dummy.next
            
