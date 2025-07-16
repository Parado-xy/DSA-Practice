
# def myAtoi( s: str) -> int:
#     # We'll use match case. 
#     # We'll manually check for space characters and everything. 
#     # If the first non zero - or white space character is zero. 
#     # We return zero. 
#     # If we'don't see a sign, we return zero. 
#     # The first non  zero value should be a sign (+ or -)
#     # We should also round down, or something like that to avoid overflows. 
#     # Return the integer obtained as the final value

#     container = ''
#     for i,value in enumerate(s):
#         if value == ' ':
#             continue
#         elif value == '+' or value == '-':
#             container += value
#         elif value.isalpha() and container == '':
#             container = 0
#             return container 
#         elif value.isalpha() and int(container) > 0:
#             return int(container)   
#         elif value == '.':
#             return int(container)         
#         elif value == '0' and container == '' and not s[i + 1].isdigit():
#             print('man')
#             return 0      
#         elif value == '0' and container == '':
#             continue                              
#         elif value.isdigit():
#             container += value    
#     if int(container) > 2**31:
#         return 2**31
#     elif int(container) < -2**31:
#         return -2**31
#     else:
#         return int(container)    



def myAtoi( s: str) -> int:
    # We'll use match case. 
    # We'll manually check for space characters and everything. 
    # If the first non zero - or white space character is zero. 
    # We return zero. 
    # If we'don't see a sign, we return zero. 
    # The first non  zero value should be a sign (+ or -)
    # We should also round down, or something like that to avoid overflows. 
    # Return the integer obtained as the final value

    dot = '.'
    signs = ['-','+']
    space = ' '
    sign_used = ''

    def convert_to_digit(s):
            try:
                number = int(s)
                return number
            except ValueError:
                return None

    if convert_to_digit(s) != None:
        if convert_to_digit(s) >= 2**31:
            return 2**31 - 1
        elif convert_to_digit(s) <= -2**31:
            return -2**31
        else:
            return convert_to_digit(s)


        
    
    


    container = ''
    for index, character in enumerate(s):
        if sign_used and character == space:
            break 
        if character == space:
            if container != '':
                break # If the container already has stuff, but we meet a white space, break. 
            continue # Skip white spaces. 
        elif character in signs:
            if sign_used == '' and container == '':
                sign_used  += character
            else:
                break    
        elif character.isalpha() and container == '': # If the first thing we encounter is an alphabet
            return 0
        elif character.isalpha(): # If the character is an alphabet, but container is not empty
            break 
        elif character == dot and container == '': # If the first character is a dot and the contrainer is empty. 
            return 0 
        elif character == dot: # If the character is a dot and the contrainer is not empty. 
            break
        elif character == '0' and  not s[index + 1].isdigit():
            container += character
            break        
        elif character.isdigit():
            container += character

    container = sign_used + container 
    if container in ['', '+', '-']:
        container = 0       
    if int(container) >= 2**31:
        return 2**31 - 1
    elif int(container) <= -2**31:
        return -2**31
    else:
        return int(container)                                            




def merge(nums1, m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 = nums1[:m]
    print(nums1)
    nums1 = nums1 + nums2
    print(nums1)
    nums1 = sorted(nums1)
    print(nums1)
        

print(merge([1,2,3,0,0,0],3,[2,5,6],3))    
