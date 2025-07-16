#!/bin/python3

def insertion_sort(arr):
    
    insertion_index = 0

    for i in range(1, len(arr)):
        key = arr[i]
        insertion_index = i - 1

        while insertion_index >= 0 and arr[insertion_index] > key:
            arr[insertion_index + 1] = arr[insertion_index] # shift the large elements 1 step backward.
            insertion_index -= 1

        arr[insertion_index + 1] = key

    return arr    

                  
numbers = [5,8,2,3,6,9]

print(insertion_sort(numbers))

