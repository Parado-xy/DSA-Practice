# Difficulty: Easy
# Question:
# Write a function to sort an array of integers in ascending order using the Insertion Sort algorithm.
# The algorithm builds the sorted array one element at a time by inserting elements into their correct positions.
#
# Example:
# Input: [5, 3, 4, 1, 2]
# Output: [1, 2, 3, 4, 5]
#
# Constraints:
# - The sorting should be done in-place.
# - Time complexity: Best case O(n), Worst and Average case O(n^2).
# - Space complexity: O(1) (in-place sorting).

def insertion_sort(arr):
    """
    Sorts an array of integers in ascending order using the Insertion Sort algorithm.

    Parameters:
        arr (list): List of integers to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    # Start from the second element (index 1) as the first element is already "sorted"
    for i in range(1, len(arr)):
        # The key is the element to be inserted into the sorted portion
        key = arr[i]
        # Initialize the position to insert the key
        j = i - 1

        # Move elements of the sorted portion that are greater than the key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position
        arr[j + 1] = key

    return arr

# Example usage 
# [3,5,4,1,2] j = 1, key = 4
# [3,4,5,1,2] j = 2, key = 1
# [1,3,4,5,2] j = 3, key = 2
# [1,2,3,4,5]
print(insertion_sort([5, 3, 4, 1, 2]))  # Output: [1, 2, 3, 4, 5]
