# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p= list1
        r=list2
        while p:
            a=p.next
            b=r.next
            if p.val<=r.val:
                p.next=r
                p=a
            elif r.val<=p.val:
                r.next=p
                r=b
        return list1 or list2
            
            
