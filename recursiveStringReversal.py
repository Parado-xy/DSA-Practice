def reverse_string(s):
    """
    Reverses a string recursively.

    Args:
        s: The string to be reversed.

    Returns:
        The reversed string.
    """

    # Base case: If the string is empty or has only one character, it's already reversed.
    if len(s) <= 1:
        return s

    # Recursive case:
    # 1. Extract the last character.
    last_char = s[-1]
    # 2. Recursively reverse the rest of the string.
    reversed_rest = reverse_string(s[:-1])
    # 3. Concatenate the last character with the reversed rest.
    return last_char + reversed_rest

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"