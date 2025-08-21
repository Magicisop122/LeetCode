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
            new.append(temp.val)
            temp = temp.next.next if temp.next else None

        temp = head.next

        while temp != None:
            new.append(temp.val)
            temp = temp.next.next if temp.next else None

        
        temp = head
        for i in range(len(new)):
            temp.val = new[i]
            temp = temp.next
        
        return head