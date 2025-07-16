# You are given two strings, string1 and string2. Your goal is to determine a new string, string3, that is formed by characters that occur in both string1 and string2 in the same order as they occur in string1.

# Characters in string3 should maintain their original sequence order from string1. If a character is repeated in string1 and string2, include that character in string3 as many times as it occurs in both strings, but not more than that.

# For example, given string1 = "apple" and string2 = "peach", the resulting string3 would be "ape".

# Your algorithm should not exceed a time complexity of O(string1.length+string2.length).

# Here's my answer that worked, but that didn't meat the time requirements:

def solution(string1, string2):
    # TODO: Implement the function here
    string1 = list(string1)
    string2 = list(string2)
    string3 = ''
    for i in range(len(string1)):
        try:
            index = string2.index(string1[i])
            string3 += string1[i]
            string2 = string2[:index] + string2[index + 1:]
        except ValueError:    
            continue 
            
    return string3         
            


# Great! Let's optimize your solution. Instead of using index() within a loop, which can be costly, 
# consider using a dictionary to count occurrences of each character in string2. 
# Then, iterate over string1 and build string3 based on these counts. 
# This approach will help you achieve the desired time complexity. 

def solution_gpt(string1, string2):
    # Create a dictionary to count occurrences of each character in string2
    count_in_string2 = {}
    for char in string2:
        count_in_string2[char] = count_in_string2.get(char, 0) + 1
    
    # Initialize the result string
    string3 = []
    
    # Iterate over string1 and build string3 based on counts in string2
    for char in string1:
        if char in count_in_string2 and count_in_string2[char] > 0:
            string3.append(char)
            count_in_string2[char] -= 1
    
    return ''.join(string3)

# Example usage:
string1 = "apple"
string2 = "peach"
print(solution_gpt(string1, string2))  # Output should be "ape"



# Question:
# You are given an array of n strings. Your task is to find the longest common suffix shared among all strings in the array. 
# A suffix is a sequence of letters at the end of a word. For instance, in the word "flying," "ing" is a suffix.

# If the given array is empty or there is no common suffix among the strings, your function should return an empty string.

# For example, given an array of strings: ["barking", "parking", "starking"], the longest common suffix is "arking".

# Solution:
def longest_common_suffix(strs):
    if not strs:
        return ""
    
    min_string = min(strs, key=len)
    ans = []
    
    for i in range(-1, -len(min_string) - 1, -1):
        # Check if all words have the same character at index i
        if all(word[i] == min_string[i] for word in strs):
            ans.append(min_string[i])
        else:
            break
    
    # Return the reversed answer as the final suffix
    return "".join(ans[::-1])

# Example usage
print(longest_common_suffix(["barking", "parking", "starking"]))  # Output: "arking"
print(longest_common_suffix(["alpha", "beta", "gamma"]))          # Output: ""
print(longest_common_suffix(["abracadabra", "dabra", "califragilisticexpialidociousdabra"]))  # Output: "dabra"

# Largest common suffix adjusted for finding the largest common prefix:
def largest_common_prefix(words):
    if not words:
        return ""
    
    min_string = min(words, key=len)
    ans = []
    
    for i in range(len(min_string)):
        # Check if all words have the same character at index i
        if all(word[i] == min_string[i] for word in words):
            ans.append(min_string[i])
        else:
            break
    
    # Return the  answer as the final prefix
    return "".join(ans)


def efficient_LCP(strs):
    # Sort the list of strings lexicographically
    # After sorting, the first and last strings will have the smallest and largest prefixes in common.
    arr = sorted(strs)
    
    # Initialize an empty string to build the longest common prefix
    ans = ''
    
    # Iterate over the characters in the shortest string (arr[0]), as the longest possible common prefix
    # can't exceed the length of the shortest string in the sorted list.
    for i in range(len(arr[0])):  # We only need to go up to the length of the smallest string
        # Check if the character at position i is the same in both the smallest and largest string.
        # If they are the same, it means this character is part of the common prefix.
        if arr[0][i] == arr[-1][i]:
            ans += arr[0][i]  # Append the character to the answer
        else:
            # If there's a mismatch, stop the loop since the common prefix ends here
            break
    
    # Return the longest common prefix found
    return ans

# Test cases to verify the function's correctness
print(efficient_LCP(["floss", "flight", "floral"]))       # Expected Output: "fl"
print(efficient_LCP(["acorns", "acornsa", "acornsac"]))   # Expected Output: "acorns"
print(efficient_LCP(["rotate", "rated", "rater"]))        # Expected Output: "rat"



# You are given a string s. Your task is to create a function that checks whether the string s consists of one repeated substring.
# If it does, the function should return the substring. If there are multiple possible answers, return the longest one. 
# If it does not consist of a repeated substring, return an empty string.
# To clarify, a "repeated substring" refers to a pattern of characters that reoccurs throughout the full string, with no characters left over. 
# For example, the string "abababab" consists of repeated substrings "ab" and "abab". On the other hand, the string "abcabcab" does not consist of a repeated substring, as the final characters "ab" do not complete the repeating pattern of "abc".

def repeat_substring(s):
    # The length of any repeated substring would be a divisor of the length of the main string
    multiples = []
    for i in range(1, len(s) + 1):
        if len(s) % i == 0:
            multiples.append(i)        
     
    ans = ''        
    # We'll start iterating from the smallest multiple to check the whole length of the string
    for multiple in multiples:
        # The amount tells us the length of the assumed substring
        amount = len(s) // multiple
        substring = s[:amount] # Let's get the first assumed substring
        # Check if repeating the substring `multiple` times results in the original string
        if substring * multiple == s:
            # If it is, set the return value to the substring
            ans = substring
            break

    return ans if ans != '' else None  # Return None if no repeating pattern is found


print(repeat_substring("abab"))  # Should return "ab"
print(repeat_substring("abcabcabc"))  # Should return "abc"
print(repeat_substring("aaaa"))  # Should return "a"
print(repeat_substring("abcd"))  # Should return None
    
print(repeat_substring("PythonPythonPython"))





# You are given a string of characters. 
# Your task is to write a function that will find and return the most common substring of a given length in the input string. 
# If two or more substrings have the same maximum frequency, you should return the lexicographically smallest one.
# For example, given the input string "bananabananaba" and a substring length of 5, your function should return "anaba", since it appears twice and is lexicographically smaller than other substrings that also appear twice (e.g., "banan").

# The expected time complexity for this task is O(str.length⋅length)
def find_most_common_substring(string: str, length: int) -> str:
  """
  Finds the most common substring of a given length in the input string.

  Args:
    string: The input string.
    length: The length of the substring to consider.

  Returns:
    The most common substring of the given length.
  """

  if length > len(string):
    return ""

  # Create a dictionary to store substring frequencies
  freq = {}
  for i in range(len(string) - length + 1):
    substring = string[i:i+length]
    freq[substring] = freq.get(substring, 0) + 1

  # Find the substring with the maximum frequency
  max_freq = 0
  most_common = ""
  for substring, count in freq.items():
    if count > max_freq:
      max_freq = count
      most_common = substring
    elif count == max_freq and substring < most_common:
      most_common = substring

  return most_common


