# Given a 32-bit signed integer, reverse digits of an integer.


# Example 1:

# Input: 123
# Output: 321

# Example 2:

# Input: -123
#Output: -321

# Example 3:

# Input: 120
# Output: 21

def reverse(x: int) -> int:
    
    result = []
    sum = 0
    is_neg = 0
    
    if x < 1:
        x = x * -1
        is_neg = 1
        
    while x != 0:
        reminder = x % 10
        x = x // 10 
        sum  = sum * 10 + reminder
        
    if sum >= 2 ** 31 - 1 or sum <= -2 ** 31:
        return 0
    
    if is_neg:
        return sum * -1
    
    return sum
