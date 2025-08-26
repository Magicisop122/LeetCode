# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:

            return None

        temp = head
        length = 0

        while temp != None:
            temp = temp.next
            length += 1

        n = length // 2

        temp = head

        while n > 1:
            temp = temp.next
            n -= 1

        temp.next = temp.next.next

        return head

        