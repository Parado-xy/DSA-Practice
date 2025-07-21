class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        answer_set = set()
        set_length = 0 
        answer_dict = {"default": 0}

        # Add something to the set if the length of the set doesn't change 
        # Then this is the longest non-repeating sub-string 
        for index, char in enumerate(s):
            for rune in s[index:]: #  "QWEERTY" = 4
                print(s[index:])
                answer_set.add(rune)
                if set_length != len(answer_set):
                    set_length += 1
                    answer_dict["".join(answer_set)] = set_length 
                else:
                    answer_dict["".join(answer_set)] = set_length 
                    set_length = 0 
                    answer_set = set()
                    break

        print(answer_dict)
        answer = max(answer_dict.values())  
                      
        # Wants us to iterate through the whole string. 
        # "QUEERTY"
        return answer

sol = Solution().lengthOfLongestSubstring(" ")
print(sol)