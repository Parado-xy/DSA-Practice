from collections import deque

def bfs(graph, start):
    # Define the bfs function which takes two parameters:
    # graph: the graph represented as an adjacency list
    # start: the starting node for the BFS traversal

    visited = set()
    # Initialize an empty set to keep track of visited nodes

    queue = deque([start])
    # Initialize a queue with the starting node
    # Using deque for efficient popping from the left

    visited.add(start)
    # Add the starting node to the set of visited nodes

    while queue:
        # Continue the loop as long as there are nodes in the queue

        vertex = queue.popleft()
        # Pop the leftmost node from the queue
        # This node is the current vertex being processed

        print(vertex, end=" ")
        # Print the current vertex followed by a space, without a newline

        for neighbor in graph[vertex]:
            # Iterate over all the neighbors of the current vertex

            if neighbor not in visited:
                # If the neighbor has not been visited yet

                visited.add(neighbor)
                # Add the neighbor to the set of visited nodes

                queue.append(neighbor)
                # Append the neighbor to the queue for future processing


graph = {
    'A': ['B', 'C'],
    'B': ['F', 'D'],
    'C': [],
    'D': ['G', 'I'],
    'E': ['H'],
    'F': ['E'],
    'G': [],
    'H': ['G'],
    'I': []
}

print(bfs(graph, 'A'))