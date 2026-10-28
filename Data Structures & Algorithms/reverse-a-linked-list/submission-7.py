# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1 -> 2 -> 3 -> 4 -> 5
2 -> 1
c.   c.n
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      prev = None
      current = head
      while current:
        next = current.next
        current.next = prev
        prev = current
        current = next      
      return prev
        

