# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k) # 3
            if not kth:
                break
            groupNext = kth.next # 4

            prev, curr = kth.next, groupPrev.next # 4, 1
            while curr != groupNext: # reverse current group
                tmp = curr.next #2
                curr.next = prev # 1 -> 4
                prev = curr # 1
                curr = tmp # 2
            
            tmp = groupPrev.next # 1
            groupPrev.next = kth # shift ptr of dummy.next
            groupPrev = tmp # shift ptr
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
