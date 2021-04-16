# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            # find place to insert the new node, either the dummy is empty or
            # current node in dummy is larger than current node in head
            # it means we need to insert the new node before the current node in dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next
        return dummy.next
