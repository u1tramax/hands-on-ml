from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        half = n // 2
        sums = [0] * half
        curr = head
        i = 0
        while curr:
            if i < half:
                sums[i] += curr.val
            else:
                sums[-i+1] += curr.val
            curr = curr.next
            i += 1
        return max(sums)
        
list = [5,4,2,1]
head = ListNode(list[0])
curr = head
for value in list[1:]:
    curr.next = ListNode(value)
    curr = curr.next
print(Solution().pairSum(head))