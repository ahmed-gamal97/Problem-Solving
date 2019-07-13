# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's #indexOf().


import re

def strStr(self, haystack: str, needle: str) -> int:
    
    if len(needle) == 0:
        return 0
    
    pattern = re.compile(needle)
    res = pattern.search(haystack) 
    if res:
        return res.span()[0]
    else:
        return -1
        
    
    for index, letter in enumerate(haystack):
        
        # Make sure to not be out of range
        if len(needle)+index <= len(haystack):
            # Search for the needle
            if needle == haystack[index:len(needle)+index]:
                return index
            else:
                continue
    return -1
    
        
