# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while (fast != None and fast.next != None) and fast != slow:
            slow = slow.next
            fast = fast.next.next
        if fast == slow:
            return True
        return False