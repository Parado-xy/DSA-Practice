def reverse_lst(numbers):
    """
    Reverses a list of integers in-place without using built-in reversal functions.

    Args:
        numbers: The list of integers to be reversed.

    Returns:
        The reversed list.
    """
    length = len(numbers)- 1
    # Iterate from the second-to-last index to the middle index, decrementing by 1.
    # This ensures we only need to swap pairs of elements.
    for i in range(length, (len(numbers) // 2) - 1, -1):
        # Swap the elements at indices i and length - i.
        # This effectively swaps elements from the two ends of the list towards the middle.
        numbers[length - i], numbers[i] = numbers[i], numbers[length - i]

    return numbers

# Shift list elements:
def shift_list_elements(ls, shift):
    # TODO: Implement the solution
    # The Shift is periodic around the length of the array. 
    zeroes = [0 for _ in range(len(ls))]
    for i,value in enumerate(ls):
        zeroes[(i + shift) % len(ls)] = value
    return zeroes


# You are given an array of n integers.
# Write a function that rearranges the array so that the middle half of the elements (considering the left and right quarters have been eliminated) move to the beginning of the array. 
# The remaining elements, the left and right quarters, should move to the end of the array. 
# If n is not divisible by 4, include the extra elements in the middle half.

# Specifically:

# Divide the array into four quarters.
# Move the second and third quarters to the front.
# Move the first and fourth quarters to the back.
# The function should modify the array in place.

# For example, if the input array is [1, 2, 3, 4, 5, 6, 7, 8], your function should rearrange the array to [3, 4, 5, 6, 1, 2, 7, 8].

# The solution should have a time complexity of O(n).

# Answer:
# Function to rearrange the array by dividing it into four quarters.
# The function moves the second and third quarters to the front,
# and then moves the first and fourth quarters to the back.

def rearrange_array(nums):
    # Calculate the quarter size
    n = len(nums)
    if n == 0:
        # Edge case for an empty array
        return nums

    thresh = n // 4  # Standard quarter size

    # If array length is divisible by 4, the quarters divide evenly
    if n % 4 == 0:
        # Rearrange using calculated quarters
        nums[:] = nums[thresh: 2 * thresh] + nums[2 * thresh: 3 * thresh] + nums[:thresh] + nums[3 * thresh:]
    
    else:
        # Handle arrays where the length isn't a perfect multiple of 4
        extra = n % 4  # Remainder elements beyond complete quarters
        
        # Shift second and third quarters to the front, with adjustment for extra elements
        nums[:] = nums[thresh: 2 * thresh] + nums[2 * thresh: 3 * thresh + extra] + nums[:thresh] + nums[3 * thresh + extra:]

# Example usage
print("Before rearrange:", [1, 2, 3, 4, 5, 6, 7, 8, 9])
rearranged_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rearrange_array(rearranged_list)
print("After rearrange:", rearranged_list)  # Expected output: [3, 4, 5, 6, 1, 2, 7, 8]
