#!/usr/bin/python3

# Implement Quick Sort

# Quick-Sort uses a pivot, then proceeds to arrange the elements of the array recursively.

def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0] # Choose the first element as pivot for easy living;

    less_than = [element for element in arr[1:] if element <= pivot]
    greater_than = [element for element in arr[1:] if element > pivot]


    return quick_sort(less_than) + [pivot] + quick_sort(greater_than)

print(quick_sort([9,3,4,5,2,11,2,34]))

# Let's try writing breadth first search
from queue import Queue

def breadth_first_search(problem: dict, initial: str, destination: str) -> bool:
    frontier = Queue()
    reached = []

    # Add the initial state to the reached array;
    reached.append(initial)
    # Add the initial state to the frontier;
    frontier.put(initial)
    # WHile the queue is not empty;
    while not frontier.empty():
        current = frontier.get()
        if current == destination:
            return True
        else:
            # Expand the current node and enqueue its children if we've not reached it before;
            for child in problem[current]:
                # Check if child is goal
                if child == destination: 
                    return True
                elif child not in reached:
                    frontier.put(child)

    return False                


graph = {
    'A': ['B', 'C'],
    'B': ['F', 'D'],
    'C': [],
    'D': ['G', 'I'],
    'E': ['H'],
    'F': ['E'],
    'G': ['K'],
    'H': ['G'],
    'I': [],
    'K': []
}

print(breadth_first_search(graph, 'A', 'K'))

# Implement best_first_search