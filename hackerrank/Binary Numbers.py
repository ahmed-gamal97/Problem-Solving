# Task 
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

# Input Format
# A single integer, n.

# Output Format
# Print a single base-10 integer denoting the maximum number of consecutive 2's in the binary representation of n.

# Sample Input 1
# 5
# Sample Output 1
# 1

# Sample Input 2
# 13
# Sample Output 2
# 2

# Explanation

# Sample Case 1: 
# The binary representation of  5 is 101 , so the maximum number of consecutive 1's is 1 .

# Sample Case 2: 
# The binary representation of  13 is 1101 , so the maximum number of consecutive 1's is 2 .

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    s = ''

    while n >= 1:
        s  = str(n%2) + s
        n = n//2


    taller = 1
    tallest = 0

    for ind in range(len(s)-1):
        if s[ind] == '1' and s[ind+1] == '1':
            taller += 1
        else:
            if taller >= tallest:
                tallest = taller
            taller = 1
    
    if taller > tallest:
            tallest = taller


print(tallest)

