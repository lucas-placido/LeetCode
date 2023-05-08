from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def last_node(nodes):
        while nodes != None:
            last_node = nodes
            nodes = nodes.next
        return last_node
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
       if list1 is None:
           return list2
       elif list2 is None:
           return list1
       output = ListNode()
       stats = True
       while stats:            
            while (list1.val <= list2.val):                
                last = Solution.last_node(output)
                last.next = ListNode(list1.val)
                list1 = list1.next
                if list1 is None:
                    stats = False
                    while list2 is not None:
                        last = Solution.last_node(output)
                        last.next = ListNode(list2.val)
                        list2 = list2.next                                                              
                    break
                
            while (stats == True) and (list2.val <= list1.val):                 
                last = Solution.last_node(output)
                last.next = ListNode(list2.val)                
                list2 = list2.next
                if list2 is None:
                    stats = False
                    while list1 is not None:
                        last = Solution.last_node(output)
                        last.next = ListNode(list1.val)
                        list1 = list1.next                        
                    break
       output = output.next
       return output     

list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
s = Solution()
output = s.mergeTwoLists(list1=list1, list2=list2)

r = []
while output is not None:
    r.append(output.val)
    output = output.next
print(r)