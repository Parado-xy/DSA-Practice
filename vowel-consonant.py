# Problem Description:
# --------------------
# Vowel-Consonant Sort (Medium)

# You are given an array of strings where each string contains a mix of vowels and consonants.
# The task is to find the difference between the number of vowels and consonants in each string
# and return the strings sorted by the absolute difference in the number of vowels and consonants.
# Strings with a smaller absolute difference come first. If two strings have the same difference,
# maintain their original relative order.

# Constraints:
# - All strings consist of only lowercase English letters.
# - Each string contains at least one letter.

# Input:
# - An array of strings `strings`.

# Output:
# - A new array where strings are sorted by their absolute vowel-consonant difference.

# Example:
# --------
# Input: 
# strings = ["apple", "banana", "kiwi", "grapefruit", "strawberry", "plum", "orange"]
# Output: 
# ['banana', 'kiwi', 'orange', 'apple', 'plum', 'grapefruit', 'strawberry']

# Explanation:
# - "banana" has 3 vowels and 3 consonants, difference = 0.
# - "kiwi" has 2 vowels and 2 consonants, difference = 0.
# - "orange" has 3 vowels and 3 consonants, difference = 0.
# - "apple" has 2 vowels and 3 consonants, difference = 1.
# - "plum" has 1 vowel and 3 consonants, difference = 2.
# - "grapefruit" has 4 vowels and 6 consonants, difference = 2.
# - "strawberry" has 2 vowels and 8 consonants, difference = 6.
# The strings are sorted by the absolute difference in vowel and consonant count.

# Approach:
# ---------
# 1. Identify the vowels in the string.
# 2. For each word in the input list, calculate the number of vowels and consonants.
# 3. Calculate the absolute difference between the vowel and consonant counts.
# 4. Use a stable sorting algorithm to maintain relative order for strings with equal differences.
# 5. Return the sorted list of strings.

# Code:

from functools import cmp_to_key

def vowel_consonant_sort(strings):
    # Define the set of vowels for quick lookup.
    vowels = {'a', 'e', 'i', 'o', 'u'}  
    
    # Helper function to calculate the absolute difference between vowels and consonants.
    def calc_difference(word):
        vowel_count = sum(1 for char in word if char in vowels)  # Count vowels.
        consonant_count = len(word) - vowel_count  # Count consonants (total length minus vowels).
        return abs(vowel_count - consonant_count)  # Return the absolute difference.
    
    # Create a list of tuples: (word, calculated difference).
    arr = [(word, calc_difference(word)) for word in strings]
    
    # Sort the array by the calculated difference.
    arr.sort(key=cmp_to_key(lambda a, b: a[1] - b[1]))
    
    # Return only the words in sorted order.
    return [word for word, _ in arr]

# Test Case:

print(vowel_consonant_sort([
    "apple",       # abs(2 - 3) = 1
    "banana",      # abs(3 - 3) = 0
    "kiwi",        # abs(2 - 2) = 0
    "grapefruit",  # abs(4 - 6) = 2
    "strawberry",  # abs(2 - 8) = 6
    "plum",        # abs(1 - 3) = 2
    "orange"       # abs(3 - 3) = 0
]))

# Expected Output:
# ['banana', 'kiwi', 'orange', 'apple', 'plum', 'grapefruit', 'strawberry']

print(chr(ord('A') + 1))