
def isSubstring(s1: str, s2: str):
    # Problem description: 
    # Assume you have a method isSubstring which checks if one word is a substring 
    # of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one 
    # call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 


    # If lengths do not match, return False
    if len(s1) > len(s2):
        return False
    
    # Create an array to store rotations. 
    rotations = []
    
    # rotate s2 at every step and add to the rotations array;
    for i in range(len(s1)):
        rotations.append(s1[i:] + s1[:i])
  

    # Check if s2 is in the list of all possible rotations.
    return s2 in rotations

print(isSubstring("waterbottle","erbottlewat"))  


# Here's a far easier solution:
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)

# If the goal is truly a subsring of s, it will be found in s+s 


    