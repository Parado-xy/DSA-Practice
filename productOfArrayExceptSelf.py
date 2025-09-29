from typing import List

class Solution:
    def productExceptSelf_brute(self, nums: List[int]) -> List[int]:
        # Create a result array. 
        res = []
        # let's iterate through the array once. 
        for i, num in enumerate(nums):
            # create a value variable that holds the total current product. 
            value = 1
            # let's iterate through the array again. 
            for j, num in enumerate(nums):
                if i != j:
                    value *= num
            # After the second loop, append the value to the result array. 
            res.append(value)
        return res

    def productExceptSelf_div(self, nums: List[int]):
        # The first step is to get the product of the whole array. 
        # And to keep a count of the number of zeroes we find. If we find more than 1, then 
        # It is guranteed that the whole array will be filled with zeroes. 
        product, zero_count = 1, 0
        for number in nums:
            # If the number doesn't equal zero
            if number != 0:
                # Calculate current product
                product *= number
            else:
                # Increment the zero counter. 
                zero_count += 1
        if zero_count > 1: return [0] * len(nums) # If we have multiple zeroes, the array will always contain strictly zero



        # Now, we can - at each index - divide the product by the value of the index. 
        result = [0] * len(nums) # A result array. 

        for i, number in enumerate(nums):
            if zero_count: 
                # If the number at the current index is not the sole zero value,
                # set this index to zero, else if it's the only zero value, 
                # set the product which contains the total array product. 
                result[i] = 0 if number else product
            else:
                # if no zeroes, just divide regularly
                result[i] = product // number
                

        return result
                    

        