"""
LeetCode 1. Two Sum
Difficulty: Easy
Category: Arrays & Hashing

Idea:
Check every pair of numbers in the array.
If the sum of two numbers equals the target, return their indices.
Use two loops to make sure we do not use the same element twice.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]