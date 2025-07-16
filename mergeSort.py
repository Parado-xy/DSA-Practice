# Difficulty: Medium
# Question:
# Write a function to sort an array of integers in ascending order using the Merge-Sort algorithm.
# The algorithm should recursively divide the array into halves, sort each half, and then merge them back together.
#
# Example:
# Input: [6, 3, 5, 1, 2, 4]
# Output: [1, 2, 3, 4, 5, 6]
#
# Constraints:
# - Sorting should not use built-in sorting functions.
# - Time complexity: O(n log n).
# - Space complexity: O(n).

def merge_sort(arr):
    """
    Sorts an array of integers in ascending order using the Merge-Sort algorithm.

    Parameters:
        arr (list): List of integers to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    # Base case: An array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: Find the middle point and split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquer: Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
        left (list): First sorted array.
        right (list): Second sorted array.

    Returns:
        list: The merged sorted array.
    """
    merged = []
    i = j = 0

    # Compare elements from both arrays and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from the left array
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Append any remaining elements from the right array
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# Example usage
print(merge_sort([6, 3, 5, 1, 2, 4]))  # Output: [1, 2, 3, 4, 5, 6]
