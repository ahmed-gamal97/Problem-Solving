# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.

# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    
    # Using that n + k = len(list) and we want to remove n element from the roght
    
    # creata a pointer that will move n elements from the left and then the another
    # pointer will start to move. So at the end the second pointer will in the n
    # postion ofrom the right. By using the fact that n + k = k + n
    npointer = head
    kpointer = head 

    counter = 0
    
    while npointer.next != None:
        npointer = npointer.next
        counter += 1
        if n < counter:
            kpointer = kpointer.next
    
    # When n equals the number of nodes
    if kpointer.next and n == counter + 1:
        head = head.next
    
    # When the linked list cosisnts of one node
    elif counter == 0 and n == 1:
        head = None
    
    else:
        kpointer.next = kpointer.next.next
    return head
