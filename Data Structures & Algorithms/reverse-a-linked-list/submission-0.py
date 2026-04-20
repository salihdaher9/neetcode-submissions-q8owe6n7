# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=None
        right=head

        while right:
            tmp=right.next
            right.next=dummy
            dummy=right
            right=tmp

        return dummy