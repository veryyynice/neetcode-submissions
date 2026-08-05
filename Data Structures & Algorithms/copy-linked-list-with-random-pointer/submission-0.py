"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #new = Node(head.val)
        if head == None:
            return None
        old = head
        #create the new linked list, add a pointer of each node created to the hashmap
        #then go through the oroginal list attaching the right thing to random of new list 
        #time O(N)
        
        #because there might be duplicates we map orig node to new node pointer instead of by value
        old2new = {}
        while old:
            new_node = Node(old.val)
            #new=new_node
            old2new[old] = new_node
            #new.next = new_node
            #new = new.next
            #new = new.next
            #new_node = new_node.next
            old = old.next
        old = head
        while old:
            curr = old2new[old]
            # if old.random == None:
            #     curr.random = None
            # else:
            if old.random:
                curr.random = old2new[old.random]
            if old.next:
                curr.next = old2new[old.next]
            old = old.next
            
        return old2new[head]
