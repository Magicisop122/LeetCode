# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # stack method with extra memory 

        # stack = []
        # curr = head

        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next

        # curr = head

        # while stack:
        #     if stack.pop() != curr.val:
        #         return False
        #     curr = curr.next
        
        # return True


        # optimal 2 pointers

        # lets find middle 

        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half

        prev = None

        while slow != None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # compare with the reversed part

        l, r = head, prev

        while r != None:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
        
        
        
        