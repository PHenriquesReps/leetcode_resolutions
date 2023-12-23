""""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        val = 0
        for i, v in enumerate(nums):
            if v < target:
                continue
            val = i
            break
        if val == 0 and nums[0] < target:
            val = len(nums)
        return val
            
        

"""
Time Complexity: 0(n)
We scan the entier array one time.
Space Complexity: 0(1)
We don't requier extra space for this solution.
"""