# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        cnt = 0
        while temp != None:
            temp = temp.next
            cnt += 1

        mid = (cnt // 2) 

        temp = head

        for _ in range(mid):
            temp = temp.next

        return temp
        

        
        