# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If no nodes, or only one node
        if(not head or not head.next):
            # Return the linked list. 
            return head 

        prev = None
        current = head 

        while (current):

            # Check if previous is equal to current. 
            if (prev and (prev.val == current.val)):
                # Cut out the current duplicate node. 
                prev.next = current.next 
                # Move to the next node
                current = current.next 
            else:
                # Else if the current value in not equal to the previous; 
                # Set new previous value; 
                prev = current
                # Move to the next node; 
                current = current.next 

        # If we're out of the loop, then duplicates must have been removed so we can return the head
        return head

        