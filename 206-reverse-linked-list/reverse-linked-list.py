# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # extra memory

        # if not head:
        #     return None

        # temp = head
        # stack = []

        # while temp != None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head

        # while temp != None:
        #     temp.val = stack.pop()
        #     temp = temp.next

        # return head

        # iterative

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



            



        


        