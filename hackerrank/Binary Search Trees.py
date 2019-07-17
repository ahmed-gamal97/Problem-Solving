# Task 
# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
# You are given a pointer, root, pointing to the root of a binary search tree.
# Complete the getHeight function provided in your editor so that it returns the #height of the binary search tree.

def getHeight(self,root):
    #Write your code here
    if not root:
        return -1
    if not root.left and not root.right:
        return 0
    
    left_height = self.getHeight(root.left)
    right_height = self.getHeight(root.right)
    return 1 + max(left_height, right_height)
