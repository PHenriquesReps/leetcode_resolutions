""""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

# Solution 1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(-1)     # creating a pre-node (fake node)
        curr = pre_head

        while list1 != None and list2 != None:      # while list1 and list2 have values
            if list1.val < list2.val:
                curr.next = list1       # assigning the connection from the current node to the next
                list1 = list1.next      # moving forward on the list
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next            # assign the new connected value to current

        if list1 != None:               # if list one still have values
            curr.next = list1           # connect the current value to the remaining linked list
        else:
            curr.next = list2
        
        return pre_head.next            # return the first real node
        

"""
Time Complexity: 0(n)
We are passing over the linked lists once.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""

# Solution 2 - Recursion

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base condition
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        #
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

"""
Time Complexity: 0(n)
We are passing over the linked lists once.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""