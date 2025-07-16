#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def authEvents(events):
    # Write your code here
    
    # Returns the ascii code. 
    def ascii_code(a):
        return ord(a)
    
    # The constants as specified by the question.
    P = 131
    M = 10**9 + 7

    # All the possibilities as specified by the constraints. 
    possibilities = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z')+ 1)] + [chr(i) for i in range(ord('0'), ord('9') + 1)]
    

    def compute_hash(string):
        value = 0
        for i, _ in enumerate(string):
            
            if i == len(string) - 2:
                value += ascii_code(string[i]) * P
            elif i == len(string) - 1:
                value += ascii_code(string[i])
            else:
                value += ascii_code(string[i]) * P**(len(string) - (i + 1))
                
        return value % M
    
    def compute_possible_hash(string):
        # This is the compute hash function
        result = [compute_hash(string)] # Add the hash of the original string to the possiilities.
        for i in possibilities:
            # compute the hash we calculated 
            result.append(compute_hash(f'{string}{i}'))
        return result

    # Let's perform the set password operation:
    commands = [i for i in events]
    # An array to keep tabs of authorization count. 
    authorized_array = []
    for i, _ in enumerate(commands):
        if commands[i][0] == 'setPassword':
            # Set hash:    
            hashed_possibilities = compute_possible_hash(commands[i][1])
            continue
        # If it's not a set password command, it's an authorization command. 
        authorized_array.append(int(int(commands[i][1]) in hashed_possibilities))


    
    # return the authorized_array
    return  authorized_array


print(authEvents([
    ["setPassword", "abc123"], 
    ["authorize", "564738291"], 
    ["authorize", "876543210"], 
    ["setPassword", "xyz789"], 
    ["authorize", "123456789"], 
    ["authorize", "987654321"]
]))     
# print(authEvents('000B')) 
# print(authEvents('000AB'))   
# # print(ord('B'))


                    
            


