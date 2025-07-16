# You are given a singly linked list and two indices, start and end (both indices are 0-based). 
# Write a Python function swap_linked_list_nodes(head: ListNode, start: int, end: int) -> ListNode that swaps the nodes of the linked list at these two provided indices. 
# The function should return the head node of the modified linked list. When swapping, you should only change the next property of a node, not the actual node values. 
# It is guaranteed that start <= end.
# For example, consider the linked list 1 -> 2 -> 3 -> 4 -> 5 and you are given start = 1 and end = 3. 
# The resulting linked list after swapping nodes at indices 1 and 3 would be:
# 11 -> 4 -> 3 -> 2 -> 5
# The expected time complexity of your solution should be O(n)
# O(n), where n is the length of the linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_linked_list_nodes(head: ListNode, start: int, end: int) -> ListNode:
    """
    Swaps the nodes of a linked list at the given indices.

    Args:
        head: The head node of the linked list.
        start: The starting index of the nodes to swap (0-based).
        end: The ending index of the nodes to swap (0-based).

    Returns:
        The head node of the modified linked list.
    """

    if start == end:
        return head

    # Find the nodes before the start and end nodes
    prev_start, curr_start = None, head
    for _ in range(start):
        prev_start = curr_start
        curr_start = curr_start.next

    prev_end, curr_end = None, head
    for _ in range(end):
        prev_end = curr_end
        curr_end = curr_end.next

    # Swap the nodes
    if prev_start:
        prev_start.next = curr_end
    else:
        head = curr_end

    if prev_end:
        prev_end.next = curr_start
    else:
        head = curr_start

    curr_start.next, curr_end.next = curr_end.next, curr_start.next

    return head

print(6 % 6)    