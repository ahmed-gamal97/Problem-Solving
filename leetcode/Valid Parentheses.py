# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true


class Solution:
    def isValid(s):
        
        if len(s) % 2 != 0:
            return False

        # Use list as a stack
        stack = []

        open_to_close = {'(':')', '{':'}', '[':']'}

        for bracket in s:
            if open_to_close.get(bracket,0) != 0:
                stack.append(bracket)
            else:
                stack_length = len(stack)
                if stack_length != 0:
                    val = stack.pop(stack_length - 1)
                    if open_to_close[val] == bracket:
                        continue
                    else:
                        return False
                    
        if len(stack) == 0:
            return True
        else:
            return False
            
