# Problem: Check for Palindrome Without Built-in Methods (Difficulty: Medium)
# You are given a string, and your task is to check whether the provided string is a palindrome.
# A string is a palindrome if it reads the same forward and backward, ignoring the case of letters 
# and any non-letter characters. You must implement this without using Python built-in methods 
# like `reverse()`, `reversed()`, or similar.

# Example:
# Input: "A man, a plan, a canal, Panama!"
# Output: True
#
# Input: "hello"
# Output: False
#
# Approach:
# - We convert all characters to lowercase manually and filter out non-letter characters.
# - Then, compare the cleaned string with its manually reversed version.
# - If both are the same, the input string is a palindrome.

def solution(input_string):
    # Helper function to manually convert an uppercase character to lowercase
    def to_lower(char):
        difference = 32
        return chr(ord(char) + difference)
    
    # Variable to hold the reversed string (ignoring non-letter characters)
    reverse = ''
    
    # Iterate over the string from the end to the beginning
    for i in range(len(input_string) - 1, -1, -1):
        if 'A' <= input_string[i] <= 'Z':
            # Convert uppercase to lowercase and add to reverse string
            input_string[i] = to_lower(input_string[i])
            reverse += input_string[i]
        elif 'a' <= input_string[i] <= 'z':
            # Add lowercase letters directly to reverse string
            reverse += input_string[i]
        else:
            # Ignore non-letter characters
            continue
    
    # Variable to hold the cleaned original string (ignoring non-letter characters)
    original = ''
    
    # Iterate over the string normally to build the original string in lowercase
    for i in range(len(input_string)):
        if 'A' <= input_string[i] <= 'Z':
            # Convert uppercase to lowercase for original string
            original += to_lower(input_string[i])
        elif 'a' <= input_string[i] <= 'z':
            # Add lowercase letters directly to original string
            original += input_string[i]
        else:
            # Ignore non-letter characters
            continue
    
    # Compare original string with reversed string, if they match, return True (palindrome)
    return original == reverse

# Example Usage:
s = "A man, a plan, a canal, Panama!"
result = solution(s)  # Expected output: True
print(result)

s = "hello"
result = solution(s)  # Expected output: False
print(result)
