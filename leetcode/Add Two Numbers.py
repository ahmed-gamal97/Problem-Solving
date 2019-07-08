# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse 
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(l1, l2):
        t = 1
        p = l1
        n1 = 0
        
        while p:
            n1 = n1 + p.val * t
            t = t * 10
            p = p.next
            
        t = 1 
        p = l2
        while p:
            n1 = n1 + p.val * t
            t = t * 10
            p = p.next
        
        if n1 == 0:
            return [0]
        
        res = []
        while n1 != 0:
            #l3 = ListNode(sum % 10)
            res.append(n1 % 10)
            n1 = n1 // 10
            
        return res
            
