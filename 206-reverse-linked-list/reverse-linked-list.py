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

        # # iterative

        # temp, prev = head, None

        # while temp != None:
        #     front = temp.next
        #     temp.next = prev
        #     prev = temp
        #     temp = front

        # return prev

        # recursive

        def reverse(head):
            if head == None or head.next == None:
                return head

            newHead = reverse(head.next)

            front = head.next
            front.next = head
            head.next = None

            return newHead

        return reverse(head)






            



        


        