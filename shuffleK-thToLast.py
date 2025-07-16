# You are given a list of n integers and a number k. Your task is to shuffle the array in such a way that, starting from the first element, every k-th element moves to the end of the array.
# For instance, if nums = [1, 2, 3, 4, 5, 6, 7, 8] and k = 3, the output should be [1, 2, 4, 5, 7, 8, 3, 6].
# Here, the 3rd element 3 and the 6th element 6 (every 3rd element starting from the first) are moved to the end of the array.

# My answer:
def shuffle_array(nums, k):
    targets = []
    count = 0
    for i in range(len(nums)):
        # Check if the current variable is a 'k-th' element in the lst
        if (i + 1) % k == 0:
            # If it is, add target values to the targets array
            targets.append(nums[count])
            # Remove the current element
            nums[:] = nums[:count] + nums[(count + 1):]
            # Decrement the count by -1 so we can backtrack. 
            count -= 1
            
        count += 1  
    # Concatenate both arrays      
    nums = nums + targets
    
    return nums       

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 4          
print(shuffle_array(nums, k)) # Expected Output: [1, 2, 3, 5, 6, 7, 9, 10, 11, 4, 8]

# Here's another versoin by ChatGPT, it works and is clean:
# Question:
# You are given a list of n integers and a number k. 
# Your task is to shuffle the array so that, starting from the first element, every k-th element moves to the end of the array.
# For instance, if nums = [1, 2, 3, 4, 5, 6, 7, 8] and k = 3, the output should be [1, 2, 4, 5, 7, 8, 3, 6].
# Explanation: The 3rd element 3 and the 6th element 6 (every 3rd element from the first) are moved to the end of the array.

def shuffle_array_gpt(nums, k):
    # List to store every k-th element
    targets = []
    
    # Loop to collect k-th elements and filter them from the list
    result = []
    for i in range(len(nums)):
        # Check if the element is in k-th position
        if (i + 1) % k == 0:
            # Move it to the targets array
            targets.append(nums[i])
        else:
            # Otherwise, keep in the result array
            result.append(nums[i])
    
    # Append all k-th elements to the end
    return result + targets

# Testing the function
print(shuffle_array_gpt([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Expected output: [1, 2, 4, 5, 7, 8, 3, 6]
