# Task 
# A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. # You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor # so that it prints the level-order traversal of the binary search tree.

# Hint: You'll find a queue helpful in completing this challenge.
	


def levelOrder(self,root):
    #Write your code here
    node_to_visit = [root]
    visited_nodes = ''
    while len(node_to_visit) > 0:
        to_visit = node_to_visit.pop(0)
        if to_visit.left:
            node_to_visit.append(to_visit.left)
        if to_visit.right:
            node_to_visit.append(to_visit.right)
        
        visited_nodes += str(to_visit.data) + ' '
    
    print(visited_nodes[:-1])
            
            






