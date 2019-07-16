# Task 
# A prime is a natural number greater than  that has no positive divisors other than  and itself.
# Given a number n, determine and print whether it's prime or not prime,

# Note: If possible, try to come up with a O(n**(1/2)) primality algorithm, or see what sort of optimizations
# you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

# Input Format
# The first line contains an integer, T , the number of test cases. 
# Each of the T subsequent lines contains an integer, n, to be tested for primality.

# Constraints
# Output Format
# For each test case, print whether  is  or  on a new line



# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

t = int(input())
nums = []

for i in range(t):
    nums.append(int(input()))



for num in nums:
    if num == 3 or num == 2:
        print('Prime')
        continue

    if num <= 1 :
        print('Not prime')
        continue
    
    start = int(math.sqrt(num))
    while start >= 2:
        if num % start == 0:    
            break
        else:
            start -= 1
    if start == 1:
        print('Prime')
    else:
        print('Not prime')
