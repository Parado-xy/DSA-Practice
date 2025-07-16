# Difficulty: Easy
# Question:
# You are given an array of integers, and your task is to sort the array using the Selection Sort method.
# In this method, the smallest integer is selected from the array and swapped with the first position. 
# This process is repeated until the array is fully sorted.
#
# Example:
# Input: [3, 1, 2, 4, 5]
# Output: [1, 2, 3, 4, 5]
#
# Note: The expected time complexity is O(n^2), and the sorting must be done in-place.

def selection_sort(arr):
    """
    Sorts an array of integers in ascending order using the Selection Sort algorithm.

    Parameters:
        arr (list): List of integers to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    for i in range(len(arr)):
        # Assume the current index holds the smallest element
        min_index = i
        
        # Find the smallest element in the remaining unsorted portion of the array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the smallest element found with the element at the current index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
print(selection_sort([3, 1, 2, 4, 5]))  # Output: [1, 2, 3, 4, 5]
