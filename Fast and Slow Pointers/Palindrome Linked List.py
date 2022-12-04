"""
leetcode link: https://leetcode.com/problems/palindrome-linked-list/

For the given head of the linked list, find out if the linked list is a palindrome or not.
Return TRUE if the linked list is a palindrome.
Otherwise, return FALSE.

Constrains:
    - The number of nodes in the list is in the range [1, 105].
    - 0 <= Node.val <= 9

Test Cases:
    - [1, 2, 2, 1] -> True
    - [1, 2] -> False
    - [1, 2, 3, 2, 1] -> True
    - [1, 2, 3, 3, 2, 1] -> True
"""

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def reverse_linked_list(head: LinkedListNode) -> LinkedListNode:
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev

def find_middle_linked_list(head: LinkedListNode) -> LinkedListNode:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow
    
def palindrome(head: LinkedListNode) -> bool:
    # find the middle of the linked list
    slow = find_middle_linked_list(head)
        
    # reverse the second half of the linked list
    curr = reverse_linked_list(slow)
    
    # check if the first half and the second half are the same
    while curr:
        if curr.data != head.data:
            return False
        curr, head = curr.next, head.next 
    
    # if the first half and the second half are the same then the linked list is a palindrome
    return True
