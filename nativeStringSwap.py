# Problem: Swap Adjacent Characters Without Built-in Methods (Difficulty: Medium)
# You are given a string `s`. The task is to return a string where every pair of adjacent characters 
# in the original string is swapped. If the string has an odd length, the last character should remain unchanged.
# You are **not allowed** to use built-in Python functions like `reverse()` or `join()` in this task.

# Example:
# Input: "abcdef"
# Output: "badcfe"
# 
# Input: "hello"
# Output: "ehllo"

# Approach:
# - First, convert the string into a list since strings are immutable in Python.
# - We iterate over the list, swapping adjacent characters in steps of two.
# - If the length of the string is odd, the last character is left unchanged.
# - After swapping, manually create the final string by appending characters one by one (without using `join()`).

def solution(s):
    # Convert the string `s` into a list to allow in-place modifications.
    s = list(s)
    
    # Case for even length strings: swap all adjacent characters.
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            s[i], s[i + 1] = s[i + 1], s[i]
    
    # Case for odd length strings: swap adjacent characters, leave the last character unchanged.
    else:
        for i in range(0, len(s) - 1, 2):
            s[i], s[i + 1] = s[i + 1], s[i]
    
    # Manually create the output string by concatenating each character.
    answer = ''
    for character in s:
        answer += character
    
    return answer

# Example Usage:
s = "abcdef"
result = solution(s)  # Expected output: "badcfe"
print(result)

s = "hello"
result = solution(s)  # Expected output: "ehllo"
print(result)
