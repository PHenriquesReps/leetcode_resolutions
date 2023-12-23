""""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""

# Solution 1 - Iteration

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # defining the starting pointers
        prev = None
        curr = head
        while(curr != None):
            temp_next = curr.next       # storing the reference of the next node
            curr.next = prev            # changing the pointer to point to the previous node
            prev = curr                 # move the previous pointer to the current node
            curr = temp_next            # move the current pointer to the next node
        
        return prev
        

"""
Time Complexity: 0(n)
We are iterating over the linked list once.
Space Complexity: 0(1)
We don't requier extra space for this solution. We are doing it in the same linked list.
"""

# Solution 2 - Recursion

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):     # base condition
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

"""
Time Complexity: 0(n)
We are iterating over the linked list once.
Space Complexity: 0(n)
We keep the entries in stack.
"""