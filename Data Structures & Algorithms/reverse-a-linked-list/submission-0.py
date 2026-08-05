# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#could use stack: until not end: insert. then pop until empty 
#
#recursion
#
#
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T O(n), M O(n)
        if not head:
            return None
        
        newHead = head
        if head.next: 
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        
        return newHead