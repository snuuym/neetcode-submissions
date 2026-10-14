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
        nodes = {None: None} #avoid no ouput when node.curr = None
        curr = head
        #copy the whole list
        while curr:
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next
        
        #assign the next and random
        curr = head
        while curr:
            nodes[curr].next = nodes[curr.next]
            nodes[curr].random = nodes[curr.random]
            curr = curr.next        

        return nodes[head]

        