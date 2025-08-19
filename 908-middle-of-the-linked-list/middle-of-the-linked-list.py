# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # O(n) solution can call it brute force

        # temp = head
        # cnt = 0
        # while temp != None:
        #     cnt += 1
        #     temp = temp.next

        # mid = (cnt // 2) + 1

        # temp = head

        # while temp != None:
        #     mid -= 1
        #     if mid == 0:
        #         break
        #     temp = temp.next

        # return temp

        # optimal approach (tortoise and hare method)

        slow, fast = head, head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow
        

        
        