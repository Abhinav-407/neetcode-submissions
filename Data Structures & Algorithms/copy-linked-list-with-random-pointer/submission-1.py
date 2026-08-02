"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
           return None

        # -------------------------
        # Pass 1: Insert copied nodes
        # -------------------------
        curr = head
        while curr:
            next_node = curr.next
            copy = Node(curr.val)

            curr.next = copy
            copy.next = next_node

            curr = next_node

        # -------------------------
        # Pass 2: Copy random pointers
        # -------------------------
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        # -------------------------
        # Pass 3: Separate the lists
        # -------------------------
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next

            # Restore original list
            curr.next = copy.next

            # Connect copied list
            if copy.next:
                copy.next = copy.next.next

            # Move to next original node
            curr = curr.next

        return copy_head