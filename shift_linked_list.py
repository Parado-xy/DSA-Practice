# You are given a singly linked list and an integer k. Your task is to write a Python function, rotate_right(linked_list, k), which rotates the linked list to the right by k places. 
# Note that k might be 0 or greater than the length of the linked list.
# Your function should take the last k nodes from the end of the list and move them to the start of the list, maintaining their original order. 
# After the rotation, return the head of the resulting linked list.
# For instance, if the linked list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, after the rotation, it should become 4 -> 5 -> 1 -> 2 -> 3.
# The expected time complexity for your solution is O(n).




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_list_node(lst):
    """
    Helper function to construct a linked list from a Python list.
    Input: List of integers (lst).
    Output: Head node of the constructed linked list.
    """
    current_node = ListNode(lst[-1])
    for val in lst[-2::-1]:
        current_node = ListNode(val, current_node)
    return current_node

def convert_to_list(head):
    """
    Helper function to convert a linked list back to a Python list.
    Input: Head node of the linked list (head).
    Output: List of integers representing the linked list.
    """
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

def rotate_right(head: ListNode, k: int) -> ListNode:
    """
    Function to rotate a singly linked list to the right by k places.
    Input: 
      - head: Head node of the linked list.
      - k: Number of positions to rotate.
    Output:
      - New head node after rotation.
    """
    # Edge case: If the list is empty or has only one node, or if k is 0, no rotation is needed.
    if not head or not head.next or k == 0:
        return head

    # Dictionary to store nodes and their previous pointers for easy access during rotation.
    index = {}
    prev = None  # Pointer to the previous node.
    current = head  # Pointer to the current node.

    # Step 1: Traverse the list and store nodes and their previous pointers in the dictionary.
    # Also, determine the length of the list.
    i = 0  # Index to keep track of positions.
    while current:
        index[f'{i}'] = [prev, current]
        prev = current
        current = current.next
        i += 1

    # The length of the linked list is the total number of nodes traversed.
    length = len(index)

    # Step 2: Normalize k to ensure it doesn't exceed the length of the list.
    k = k % length

    # If k is 0 after normalization, the list remains unchanged.
    if k == 0:
        return head

    # Step 3: Calculate the new head position after rotation.
    # The new head will be the (length - k)-th node in the list.
    new_head_index = length - k

    # Step 4: Adjust pointers to perform the rotation.
    # Break the link at the new head's previous node.
    index[f'{new_head_index}'][0].next = None

    # Connect the tail node to the original head to complete the rotation.
    index[f'{length - 1}'][1].next = index[f'{0}'][1]

    # Step 5: Return the new head of the rotated list.
    return index[f'{new_head_index}'][1]

# Example usage:
# Construct the linked list from a Python list.
head = construct_list_node([1, 2, 3, 4, 5])

# Rotate the list to the right by 2 places.
rotated_head = rotate_right(head, 2)

# Convert the rotated linked list back to a Python list and print it.
print(convert_to_list(rotated_head))  # Output: [4, 5, 1, 2, 3]
