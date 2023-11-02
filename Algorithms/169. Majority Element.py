""""
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = None
        for num in nums:
            if count == 0:
                majority = num
                count += 1
            elif majority != num:
                count = count - 1
            else:
                count += 1
        return majority
        

"""
Time Complexity: 0(n)
We scan the entier array one time.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""