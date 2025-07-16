# You have been given an array of n integers. Your task is to write a function that reverses the array in groups of k size, and if the last group has fewer than k elements, reverse all of them. 
# Return the newly organized array after the groups have been reversed.
# For example, given the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be: [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]. 
# The first three elements are reversed to get [3, 2, 1], the next three become [6, 5, 4], the following three are [9, 8, 7], and the final one remains [10] as there are fewer than k elements remaining.


def solution(numbers, k):
    """
    Reverses the given array in groups of size k.

    Args:
        numbers: The input array of integers.
        k: The size of the groups to be reversed.

    Returns:
        The array with reversed groups.
    """

    for i in range(1, len(numbers), k):
        # Calculate the start and end indices of the current group.
        start = i - 1
        end = min(i + k - 1, len(numbers) - 1)  # Adjust end index to avoid out-of-bounds access

        # Reverse the sublist using extended slicing with a negative step
        numbers[start:end+1] = numbers[start:end+1][::-1]

    return numbers

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 89], 3))

# Explanation:
# Iterating over the array in steps of k:

# for i in range(1, len(numbers), k):
# This loop iterates over the indices of the array, starting from 1 and incrementing by k each time. This ensures we process the array in groups of size k.
# Calculating start and end indices:

# start = i - 1
# This calculates the starting index of the current group.
# end = min(i + k - 1, len(numbers) - 1)
# This calculates the ending index of the current group, taking into account the possibility of the group being smaller than k elements. The min function ensures that we don't access elements beyond the array's bounds.
# Reversing the sublist:

# numbers[start:end+1] = numbers[start:end+1][::-1]
# This line efficiently reverses the sublist using extended slicing with a negative step. The [::-1] slice notation reverses the elements of the sublist.
# Python's graceful handling of out-of-bounds slicing ensures that the end+1 index is automatically adjusted to the last valid index if necessary, preventing errors.
# By combining these steps, the function effectively reverses the array in groups of k elements, handling the last group correctly even if it's smaller than k.

