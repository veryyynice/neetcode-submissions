# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #9 +9 = 81
        #prob we add to one of the lists for O(1) space
        dummy = ListNode()
        carry = 0
        curr = dummy
        val = 0
        while l1 or l2 or carry:
            # if l1 == None:
            #     val = 0+ l2.val+carry
            # elif l2 == None:
            #     val = 0+l1.val+carry
            # else: 
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val

            val = val1+val2+carry
            # if curr>=10:
            carry = val//10
            val = val%10
            curr.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next            
