# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cnt = 0
        temp = head

        while temp != None:
            cnt += 1
            temp = temp.next

        if cnt == n:
            newHead = head.next
            return newHead

        res = cnt - n
        temp = head

        while temp != None:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        # delNode = temp.next
        temp.next = temp.next.next
        return head