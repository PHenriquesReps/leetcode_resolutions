""""
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
           result = result ^ num
        return result

"""
Time Complexity: 0(n)
We scan the entier array one time.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""