# Problem: Case Transformation Without Built-in Methods (Difficulty: Easy)
# Given a string `input_string`, the task is to transform all lowercase letters to uppercase 
# and all uppercase letters to lowercase. Non-letter characters should remain unchanged.
# Importantly, you are **not allowed** to use Python's built-in string methods like `lower()` or `upper()`.
# You must manually handle the ASCII conversion of characters.

# Example:
# Input: "HelLo WoRld 123"
# Output: "hELlO wOrLD 123"

# Approach:
# - Each letter has an ASCII value.
#   For lowercase letters 'a' to 'z', the ASCII values are between 97 and 122.
#   For uppercase letters 'A' to 'Z', the ASCII values are between 65 and 90.
# - The difference between uppercase and lowercase letters in ASCII is 32.
#   For example, `ord('A')` is 65, and `ord('a')` is 97, so we can shift between cases by adding/subtracting 32.

def solution(input_string):
    # Convert the input string to a list of characters (since strings in Python are immutable).
    input_string = list(input_string)
    
    # Function to convert a lowercase character to uppercase.
    def to_upper(char):
        # ASCII difference between uppercase and lowercase letters is 32.
        difference = 32
        return chr(ord(char) - difference)

    # Function to convert an uppercase character to lowercase.
    def to_lower(char):
        # ASCII difference between uppercase and lowercase letters is 32.
        difference = 32
        return chr(ord(char) + difference)
    
    # Iterate over each character in the input string.
    for i, _ in enumerate(input_string):
        # If the character is a lowercase letter ('a' to 'z'), convert it to uppercase.
        if 'a' <= input_string[i] <= 'z':
            input_string[i] = to_upper(input_string[i])
        # If the character is an uppercase letter ('A' to 'Z'), convert it to lowercase.
        elif 'A' <= input_string[i] <= 'Z':
            input_string[i] = to_lower(input_string[i])
        # If the character is neither, leave it unchanged.
        else:
            continue
    
    # Join the list of characters back into a string and return the result.
    return "".join(input_string)

# Example Usage:
input_string = "HelLo WoRld 123"
result = solution(input_string)  # Expected output: "hELlO wOrLD 123"
print(result)
