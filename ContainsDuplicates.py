""""
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""



"""Approach 1:
using bruteforce : two loops
Time complexity : O(n²)
space complexity :O(1)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False  



"""Approach 2:
using hashmap : num -> True
Time complexity : O(n)
space complexity : O(n)
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {} 
        for num in nums:
            if num in seen:   
                return True
            seen[num] = True  
        return False
