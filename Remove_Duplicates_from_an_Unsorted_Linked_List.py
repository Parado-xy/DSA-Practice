
#   node = {value, rest: {value, rest: {value, rest:null}}}

import random

 # Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

#    Method to append new nodes to the list
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

#    Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage to create an unsorted linked list with random values
def generate_random_linked_list(size, lower_bound=1, upper_bound=10):
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(lower_bound, upper_bound))
    return linked_list

# Generate a random linked list with 10 nodes, values between 1 and 10
random_linked_list = generate_random_linked_list(10)

# Printing the random linked list
random_linked_list.print_list()



def remove_duplicates(node):
    # Create an array for storing seen values.
    store = []
    # Store a refrence to the beginning of the linked list. 
    returned = node.head
    # Start the previous and current pointers at the beginning of the node. 
    prev = node.head
    current = node.head
    
    # Check if the current node is valid, i.e not None
    while current:
            if current.data in store:
                # Set the next pointer one step forward skipping the current value in the process. 
                prev.next = current.next
                # Then set the new current value to be used as the value prev.next now points to, the new 'next' value.
                current = prev.next

            else:
                # If we have not seen the data before, add it to the array of seen values. 
                store.append(current.data)
                # Print out current and seen values for debugging purposes
                # print(f'previous {prev.data} when current: {current.data}')
                # Set the previous value to the current value, thereby updating the pointer by 1
                prev = current
                # Set the current value to the actual current value in the linked list. 
                current = current.next               
    return returned

# Function to manually traverse the linked list and print each node's value
def manual_traverse(linked_list):
    
    current = linked_list
    while current:
        print(f"{current.data} ->", end=' ')
        current = current.next
    print("None")

# # Remove duplicates and print to stdout
# manual_traverse(remove_duplicates(random_linked_list))

def remove_duplicates_bufferless(node):
    current = node.head
    
    while current.next:
        # runner and current start at  the head of the linked list. 
        runner = current
        # While runner has somewhere to go to next,
        while runner.next:
            print(f'{current.data} == {runner.data}')
            # Check if the current value matches the runner's next position
            if current.data == runner.next.data:
                # If the current value matches where the runner is about to go, the runner jumps over it
                # Cutting it out of the loop in the process.
                runner.next = runner.next.next
            else:
                # If the current value doesn't match where the runner will go to next,
                # Allow the runner to go there.
                runner = runner.next    
        # move the current value to the next node and do this all over again.         
        current = current.next    
    # return the begining of the original linked list. 
    return node.head

# Remove duplicates and print to stdout
manual_traverse(remove_duplicates_bufferless(random_linked_list))


