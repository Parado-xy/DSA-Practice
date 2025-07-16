# Given the head of a sorted linked list,
# delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list. 
# Return the linked list sorted as well.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Create a dummy node
        dummy = ListNode(0, head)
        prev = dummy  # Points to the node before the current sequence of duplicates
        
        while head:
            # If the current node is a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Connect prev node to the node after the duplicates
                prev.next = head.next
            else:
                # Move prev pointer if no duplicate
                prev = prev.next
            
            # Move head pointer
            head = head.next
        
        return dummy.next
