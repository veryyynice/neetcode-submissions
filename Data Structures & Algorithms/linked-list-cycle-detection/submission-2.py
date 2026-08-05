# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()
        # while head.next != None:
        #     if head not in visited:
        #         visited.add(head)
        #         head = head.next
        #     else: 
        #         return True
        # return False
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True

        return False