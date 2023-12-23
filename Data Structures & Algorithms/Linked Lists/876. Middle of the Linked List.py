""""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

"""

# Solution 1

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        mid = (count//2) + 1
        i = 1
        temp = head
        while i < mid:
            temp = temp.next
            i += 1
        return temp
        

"""
Time Complexity: 0(2n) ~ 0(n)
We are passing 3 times over the linked list.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""

# Solution 2

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slower = head
        faster = head
        while(faster != None and faster.next != None):
            slower = slower.next
            faster = faster.next.next
        return slower

"""
Time Complexity: 0(n)
We are passing over the linked lists once.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""