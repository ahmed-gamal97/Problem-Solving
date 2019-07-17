# Task 
# Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, # print the following 3 lines:

# Array is sorted in numSwaps swaps. where numSwaps is the number of swaps that took place.
# First Element: firstElement where firstElement is the first element in the sorted array.
# Last Element: lastElement  where lastElement is the last element in the sorted array.

# Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

# Input Format

# The first line contains an integer, n, denoting the number of elements in array a. 
# The second line contains n space-separated integers describing the respective values of a0,a1,.... .

# Output Format

# Print the following three lines of output:

# Array is sorted in numSwaps swaps. where numSwaps is the number of swaps that took place.
# First Element: firstElement where firstElement is the first element in the sorted array.
# Last Element: lastElement where lastElement is the last element in the sorted array.


# Sample Input 1
# 3
# 3 2 1

# Sample Output 1
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_counter = 0

for j in range(len(a)):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            swap_counter += 1
            a[i], a[i+1] = a[i+1], a[i]



print('Array is sorted in {} swaps.'.format(swap_counter))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))

