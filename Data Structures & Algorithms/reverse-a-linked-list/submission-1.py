# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None,prev=None):
         self.val = val
         self.next = next
         self.prev = prev 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr:
            v=curr.next
            curr.next=prev
            prev=curr
            curr=v
        return prev




        