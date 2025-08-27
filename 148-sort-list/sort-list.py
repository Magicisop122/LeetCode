# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []

        i = head

        while i != None:
            temp.append(i.val)
            i = i.next

        temp.sort()

        dummy = ListNode(0)
        curr = dummy

        for j in temp:
            curr.next = ListNode(j)
            curr = curr.next

        return dummy.next
        
                