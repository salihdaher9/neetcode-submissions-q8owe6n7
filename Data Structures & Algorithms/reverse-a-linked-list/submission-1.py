# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=None
        r=head
        if not r :
            return prev
        
        while r:
            temp=r.next
            r.next=prev
            prev=r
            r=temp
                
        return prev
        

