""""
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
class Solution:
    def reverse(self, nums:list, start:int, end:int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end - 1


    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k%size
        self.reverse(nums,0,size-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k, size-1)
        

"""
Time Complexity: 0(n)
We scan the entier array one time.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""