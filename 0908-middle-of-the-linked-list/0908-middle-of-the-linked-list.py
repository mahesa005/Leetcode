# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ctr = head
        splitted = head
        length = 0
        mid = 0
        while ctr != None:
            length += 1
            ctr = ctr.next
        if length % 2 == 1:
            mid = length//2 + 1
            mid = int(mid)
            ctr = 1
            found = False
            while splitted != None and found == False:
                if ctr != mid:
                    splitted = splitted.next
                    ctr += 1
                else:
                    head = splitted
                    found = True
        else:
            mid = length/2 + 1
            mid = int(mid)
            ctr = 1
            found = False
            while splitted != None and found == False:
                if ctr != mid:
                    splitted = splitted.next
                    ctr += 1
                else:
                    head = splitted
                    found = True
        return splitted