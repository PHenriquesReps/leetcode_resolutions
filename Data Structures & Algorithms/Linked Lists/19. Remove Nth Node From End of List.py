""""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

# Solution 1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head

        if temp.next == None:
            return temp.next
        while temp:
            count += 1
            temp = temp.next
        i = 1
        temp = head
        if count == n:
            return head.next

        while i < (count - n):
            temp = temp.next
            i += 1
        temp.next = temp.next.next

        return head
        

"""
Time Complexity: 0(2n) ~ 0(n)
We are passing 2 times over the linked list.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""

# Solution 2

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prehead.next = head
        slow = prehead
        fast = prehead

        i = 1

        while i <= n:
            fast = fast.next
            i += 1
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return prehead.next

"""
Time Complexity: 0(n)
We are passing over the linked lists once.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""