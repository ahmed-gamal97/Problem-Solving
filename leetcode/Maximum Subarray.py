# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its # sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.4


def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
	# Using greedy Algorithms

    max_current = max_global = nums[0]
    max_c = max_g = [nums[0]]

    for ind in range(1, len(nums), 1):
        max_current = max(nums[ind], max_current + nums[ind])
        
        # If You want to return the subarray itself
        #-------------------------------------
        if  nums[ind] > sum(max_c + [nums[ind]]):
            max_c = [nums[ind]]
        else:
            max_c = max_c + [nums[ind]]
        if sum(max_c) > sum(max_g):
            max_g = max_c        
        #-------------------------------------
        
        if max_current > max_global:
            max_global = max_current
        
        
    return max_global
    
    
        
        

