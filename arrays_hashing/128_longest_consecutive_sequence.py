"""
LeetCode 128. Longest Consecutive Sequence
Difficulty: Medium
Category: Arrays & Hashing

Idea:
Sort the array first.
Then count the length of each consecutive sequence.
Use current to track the current sequence length.
Use longest to store the maximum sequence length.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 1
        longest = 1
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] - nums[i] == 1:
                current += 1
            else:
                current = 1
            
            longest = max(longest, current)

        return longest
        
# -> Accepted, but not O(n) time, so ideal solution:

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest