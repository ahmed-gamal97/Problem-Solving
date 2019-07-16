# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it # were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0


def searchInsert(nums: List[int], target: int) -> int:
    
    # Simple
    length = len(nums)
    if target > nums[-1]:
	    return length
    
    for i in range(length):
        if nums[i] >= target:
            return i
    
    # Also simple but it uses enumerate instead        
    for ind, num in enumerate(nums):
        if num >= target and ind != 0:
            return ind
        elif num >= target and ind == 0:
            return 0
        
    return len(nums)
