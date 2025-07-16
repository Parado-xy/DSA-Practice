# You are provided with two input lists that contain n and m integers, respectively. 
# Both lists are sorted in non-decreasing order — i.e., every element is either equal to or larger than the preceding one.
# Your task is to return a new list that results from merging the two input lists so that the final output list is also in non-decreasing order. 
# It should contain all the elements of the two lists, maintaining their order within the lists.
# Your solution should not use the built-in sort function of Python but should instead use a technique similar to the one used in the lesson. 
# The expected time complexity is O(n+m).
# For instance, if the two input lists are [1, 3, 5, 7, 9] and [2, 2, 3, 4, 6, 6], your function should return [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 9].

# def solution(l1, l2):
#     l1_pointer = 0
#     l2_pointer = 0
#     result = []
    
#     for i in range(len(l1) + len(l2)):
#         try:
#             if l1[l1_pointer] < l2[l2_pointer]:
#                 result.append(l1[l1_pointer])
#                 l1_pointer += 1
#             else:
#                 result.append(l2[l2_pointer])
#                 l2_pointer += 1
            
#             if l1[l1_pointer] == l2[l2_pointer]:
#                 result.append(l1[l1_pointer])
#                 result.append(l2[l2_pointer])
#                 l1_pointer += 1
#                 l2_pointer += 1    
#         except IndexError:
#             break         
 
#     if l2_pointer < len(l2):
#         result = result + l2[l2_pointer:] 
      
#     if l1_pointer < len(l1):
#         result = result + l1[l1_pointer:]
        
#     return result   
    
# print( solution([1, 3, 5, 7, 9], [2, 2, 3, 4, 6, 6]))   
# 
def solution(l1, l2):
    l1_pointer = 0
    l2_pointer = 0
    result = []

    # Merge the two lists until we reach the end of one of them
    while l1_pointer < len(l1) and l2_pointer < len(l2):
        if l1[l1_pointer] < l2[l2_pointer]:
            result.append(l1[l1_pointer])
            l1_pointer += 1
        else:
            result.append(l2[l2_pointer])
            l2_pointer += 1

    # Append any remaining elements from l1 or l2
    if l1_pointer < len(l1):
        result.extend(l1[l1_pointer:])
    if l2_pointer < len(l2):
        result.extend(l2[l2_pointer:])

    return result

# Test the function with the provided example
print(solution([1, 3, 5, 7, 9], [2, 2, 3, 4, 6, 6]))




# You are given two sorted lists, each containing n integers. Your task is to merge these two lists into a new list such that:

# The resulting list is sorted in descending order.
# If there are duplicate elements in the two lists, they should be merged so that each duplicate appears only once in the final list.
# For instance, if you are given two lists, [1, 2, 3, 4, 5] and [3, 4, 5, 6, 7], your function should return [7, 6, 5, 4, 3, 2, 1] as the merged list.
                      
def merge_sorted_lists_descending_unique(l1, l2):
    l1_pointer = 0
    l2_pointer = 0
    result = []

    # Merge the two lists until we reach the end of one of them
    while l1_pointer < len(l1) and l2_pointer < len(l2):
        if l1[l1_pointer] < l2[l2_pointer]:
            if l1[l1_pointer] in result:
                l1_pointer += 1
            else:    
                result.append(l1[l1_pointer])
                l1_pointer += 1
        else:
            if l2[l2_pointer]  in result:
                l2_pointer += 1
            else:    
                result.append(l2[l2_pointer])
                l2_pointer += 1

# Append remaining elements from the non-exhausted list
    while l1_pointer < len(l1):
        if l1[l1_pointer] not in result:
            result.append(l1[l1_pointer])
        l1_pointer += 1

    while l2_pointer < len(l2):
        if l2[l2_pointer] not in result:
            result.append(l2[l2_pointer])
        l2_pointer += 1

    return result[::-1]                      


# Imagine you are given two sorted lists of integers, list1 and list2. 
# Your task is to write a Python function that will return a new sorted list that comprises elements from list1 and list2, but without any common elements in both lists. 
# This new list must also be sorted in ascending order.
# For instance, if you are given list1 = [2, 5, 7, 10] and list2 = [1, 5, 9], your function remove_common_elements([2, 5, 7, 10], [1, 5, 9]) should return [1, 2, 7, 9, 10] because 5 is a common element in both lists and should be removed.
def remove_common_elements(list1, list2):
    pointer_1 = 0
    pointer_2 = 0
    result = []
    
    while pointer_1 < len(list1) and pointer_2 < len(list2):
        if list1[pointer_1] < list2[pointer_2]:
            result.append(list1[pointer_1])
            pointer_1 += 1
        elif list1[pointer_1] > list2[pointer_2]:
            result.append(list2[pointer_2])
            pointer_2 += 1
        else:
            # If both elements are equal, and therefore duplicates, skip.
            pointer_1 += 1
            pointer_2 += 1
            
    while pointer_1 < len(list1):
        if list1[pointer_1] not in result:
            result.append(list1[pointer_1])
        pointer_1 += 1

    while pointer_2 < len(list2):
        if list2[pointer_2] not in result:
            result.append(list2[pointer_2])
        pointer_2 += 1        
    return result                






















