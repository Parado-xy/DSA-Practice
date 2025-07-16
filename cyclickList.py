# You are given a linked list, and you are required to detect if a cycle exists in the linked list. 
# A linked list is said to contain a cycle if a node's next pointer points back to one of the previous nodes in the list. 
# Given the head of the linked list head, return True if the linked list contains a cycle and False otherwise.
# You need to solve this using O(1) of additional memory.


# There are 2 approaches to this. One if you wanna do it in constant space, O(1)
# The O(n) approach is to traverse while putting each node in an array.
# If the current node is ever in the array, then it's cyclic. 
# The O(1) approach requires using 2 pointers. Start one at head, and one at head.next.
# The fast one should move 2 steps, skipping one node. If the List is cyclic. The fast pointer will at some point be at the same location as the slow pointer.

class ListNode:
    """
    Definition for a singly linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    """
    Function to detect if a singly linked list contains a cycle.
    Approach: Use two pointers (fast and slow) to detect the cycle in O(1) additional memory.
    Input: 
      - head: The head node of the linked list.
    Output:
      - True if the linked list contains a cycle, False otherwise.
    """
    # Edge case: If the list is empty or has only one node, it can't have a cycle.
    if not head or not head.next:
        return False

    # Initialize two pointers: slow and fast.
    slow = head
    fast = head

    # Traverse the list with the two pointers.
    # Slow pointer moves one step at a time.
    # Fast pointer moves two steps at a time.
    while fast and fast.next:
        slow = slow.next  # Move slow pointer one step forward.
        fast = fast.next.next  # Move fast pointer two steps forward.        
        # If the two pointers meet, there is a cycle.
        if fast == slow:
            return True


    # If we reach the end of the list, there is no cycle.
    return False

# Test case 1: A cyclic linked list.
# Create a linked list with 100,000 nodes where the last node points back to the first node.
nodes = [ListNode(i) for i in range(1, 100001)]
for i in range(100000):
    nodes[i].next = nodes[(i + 1) % 100000]  # The last node connects to the first node, forming a cycle.
head6 = nodes[0]
print(hasCycle(head6))  # Expected output: True

# Test case 2: A non-cyclic linked list.
# Create a simple linked list with no cycles: 1 -> 2 -> 2 -> 1 -> None
head4 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(hasCycle(head4))  # Expected output: False
