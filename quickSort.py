# Difficulty: Medium
# Question:
# Write a function to sort an array of integers in ascending order using the Quick Sort algorithm.
# The algorithm selects a "pivot" element and partitions the array so that elements smaller than the pivot
# are placed to the left, and elements greater than the pivot are placed to the right.
# This process is repeated recursively on the subarrays.
#
# Example:
# Input: [6, 3, 5, 1, 2, 4]
# Output: [1, 2, 3, 4, 5, 6]
#
# Constraints:
# - Sorting should not use built-in sorting functions.
# - Time complexity: Best and Average Case: O(n log n), Worst Case: O(n^2).
# - Space complexity: O(log n) on average (due to recursion).

import timeit

def quick_sort(arr):
    """
    Sorts an array of integers in ascending order using the Quick Sort algorithm.

    Parameters:
        arr (list): List of integers to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    # Base case: An array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Select the pivot (choosing the last element for simplicity)
    pivot = arr[-1]
    
    # Partition the array into two halves
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Recursively sort the left and right subarrays, then combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
print(quick_sort([6, 3, 5, 1, 2, 4]))  # Output: [1, 2, 3, 4, 5, 6]
