# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

# Return the length of the longest cycle in the graph. If no cycle exists, return -1.

# A cycle is a path that starts and ends at the same node.

 

# Example 1:


# Input: edges = [3,3,4,2,3]
# Output: 3
# Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
# The length of this cycle is 3, so 3 is returned.
# Example 2:


# Input: edges = [2,-1,3,1]
# Output: -1
# Explanation: There are no cycles in this graph.


from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int | float:
        # Initialize the number of nodes in the edge list
        num_nodes = len(edges)
        # Create a visitation status list to keep track of visited nodes
        visited = [False] * num_nodes
        # Initialize the answer to -1, which stands for no cycle found
        longest_cycle_length = -1
      
        # Iterate over each node
        for node in range(num_nodes):
            # Skip processing if the current node has been visited
            if visited[node]:
                continue
          
            # Initialize the node for cycle checking
            current_node = node
            # Initialize list to store nodes in the current cycle
            node_cycle = []
          
            # Continue traversing the graph unless we hit a node
            # that points to -1 or it has been visited
            while current_node != -1 and not visited[current_node]:
                # Mark the node as visited
                visited[current_node] = True
                # Append current node to the cycle
                node_cycle.append(current_node)
                # Move to the next node in the graph
                current_node = edges[current_node]
          
            # If the end of an edge chain points to -1, a cycle isn't possible
            if current_node == -1:
                continue
          
            # Calculate the length of the cycle. To do this, we find the index of
            # the node that we revisited which caused the cycle detection
            cycle_length = len(node_cycle)
            # Find the starting index of the cycle within node_cycle list
            cycle_start_index = next((k for k in range(cycle_length) if node_cycle[k] == current_node), float('inf'))
            # Update the longest_cycle_length with the maximum
            longest_cycle_length = max(longest_cycle_length, cycle_length - cycle_start_index)
      
        # Return the length of the longest cycle, or -1 if no cycle is found
        return longest_cycle_length
        