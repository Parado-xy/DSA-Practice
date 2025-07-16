from typing import List, Optional

# Below is a link to the selection sort algorithm.
# URL: https://en.wikipedia.org/wiki/Selection_sort

def second_max(nums: List[int]) -> Optional[int]:
    """
    Given a list of integers, find the second-largest unique integer.
    If fewer than two unique integers are present, return None.
    
    Difficulty: Medium
    
    Problem Analysis:
    - This problem requires finding the second-largest unique integer in the list.
    - The function is constrained not to use Python’s built-in sorting or max functions,
      requiring a custom approach for finding unique values and sorting.
    - Edge cases include lists with fewer than two unique values, and handling duplicates.
    
    Solution Analysis:
    - Uses a custom min_sort function to sort the list in ascending order.
    - Converts the input list into a set to filter out duplicates.
    - Checks for the second-largest integer after sorting.

    :param nums: List of integers to analyze
    :return: The second-largest unique integer or None
    """

    # Helper function to perform selection sort in ascending order.
    def min_sort(nums):
        for i in range(len(nums)):
            # Assume the first element in the unsorted section is the minimum.
            current_min = i
            # Check the remaining elements for a smaller value.
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[current_min]:
                    current_min = j
            # Swap the found minimum element with the first element of the unsorted section.
            nums[i], nums[current_min] = nums[current_min], nums[i]
        return nums

    # Convert the list to a set to remove duplicates, then back to a list for sorting.
    sorted_array = min_sort(list(set(nums)))

    # Return the second-to-last element if there are at least two unique values.
    return sorted_array[-2] if len(sorted_array) >= 2 else None

# Example usage
# print(second_max([1, 1, -1, 3, 5, 7, -4, 9, 4]))  # Expected output: 7

class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            value = list(str(x))
            for i in range(len(value) - 1, -1, -1):
                value[len(value) - 1 - i]  = value[i]
            value = int("".join(value))
            return True if value / x == 1.0 else False
        except Exception:
            return False 
        
# word = Solution()
# print(word.isPalindrome(213))  
# print(word.isPalindrome(1001))  # Expected: True
# print(word.isPalindrome(7))  # Expected: True
# print(word.isPalindrome(1234567890123456789))  # Expected: False
# print(word.isPalindrome(1234567890987654321))  # Expected: True

def is_palindrome(num):

    if num < 0:
        return False
    
    saved = num
    answer = 0
    while num > 0:
        index = num % 10
        answer = answer * 10 + index
        num //= 10
    return saved == answer    

print(is_palindrome(1_000_890))



