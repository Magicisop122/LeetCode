# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        new = []

        temp = head

        while temp != None:
            new.append(temp)
            temp = temp.next.next if temp.next else None

        temp = head.next

        while temp != None:
            new.append(temp)
            temp = temp.next.next if temp.next else None

        
        for i in range(len(new) - 1):
            new[i].next = new[i + 1]
        new[-1].next = None

        return new[0]