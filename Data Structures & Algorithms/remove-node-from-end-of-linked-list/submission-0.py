# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length+=1
            node = node.next
        index = length - n
        if index == 0:
            head = head.next
        else:
            i = 0
            curr = head
            prev = ListNode()
            while i<index:
                prev = curr
                curr = curr.next
                i+=1
            prev.next = curr.next        
        return head
        

        