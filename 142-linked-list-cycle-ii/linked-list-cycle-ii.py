# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # brute force O(n) space

        # hashmap = {}

        # curr = head

        # while curr != None:
        #     if curr in hashmap:
        #         return curr

        #     hashmap[curr] = 1

        #     curr = curr.next

        # return None

        # optimal approach tortoise and hare method

        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next 
                    fast = fast.next
                return slow
                    

        return None

        