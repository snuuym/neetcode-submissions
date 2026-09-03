# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:   
        if not head:
            return False
        seen = set()
        curr = head
        while curr:
            seen.add(curr)
            if not curr.next:
                return False
            else:
                curr =curr.next 
                if curr in seen:
                    return True

        