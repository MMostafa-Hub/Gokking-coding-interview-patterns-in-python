"""
leetcode link: https://leetcode.com/problems/middle-of-the-linked-list/

Given a singly linked list, return the middle node of the linked list.
If the number of nodes in the linked list is even, return the second middle node.

Constraints:
    - 1 <= The number of nodes in the list <= 100.
    - 1 <= Node.val <= 100.

Test Cases:
    - [1, 2, 3, 4, 5] -> 3
    - [1, 2, 3, 4, 5, 6] -> 4
    
"""

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
def get_middle_node(head: LinkedListNode) -> int:
    fast = slow = head
    # if fast pointer reaches the end of the linked list
    # then the slow pointer will be at the middle of the linked list
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow.data