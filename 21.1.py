from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
           return list2
        elif not list2:
           return list1

        output = ListNode()
        tail = output
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2
        return output.next
        
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
s = Solution()
output = s.mergeTwoLists(list1=list1, list2=list2)

r = []
while output is not None:
    r.append(output.val)
    output = output.next
print(r)        