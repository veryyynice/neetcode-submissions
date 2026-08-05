# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #we do range(len(head)), n-1-> 0 , altenating
        #[0, n-1, 1, n-2, 2, n-3, ...]

        slow,fast = head,head.next #prob both can be same
        #get middle point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second= slow.next
        slow.next = None #splitting list

        #previous ode 
        prev= slow.next=None #???
        #reverse
        while second:
            tmp=second.next
            second.next = prev
            prev= second
            second = tmp

        #merge two half

        first,second =head,prev

        while second:
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2

            