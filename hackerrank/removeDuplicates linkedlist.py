# Task 
# A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, # pointing to another node (i.e.: the next node in a list).

# A removeDuplicates function is declared in your editor, which takes a pointer to the head node of a linked list as a parameter. # Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.

# Note: The head pointer may be null, indicating that the list is empty. Be sure to reset your next pointer when performing deletions to # avoid breaking the list.


def removeDuplicates(self,head):

    #Write your code here
    one_before, current = head, head
    if head == None or current.next == None:
        return head

    numbers = []
    

    numbers.append(current.data)
    current = current.next


    while current:
        if current.data not in numbers:
            numbers.append(current.data)
            one_before = current        
            current = current.next
        else:
            one_before.next = current.next
            current.next = None
            current = one_before.next

            

    return head



