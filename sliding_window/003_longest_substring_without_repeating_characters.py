"""
LeetCode 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Category: Sliding Window / String

Idea:
Use a list as the current substring window.
Loop through each character in the string.
If the current character already exists in the window,
remove characters from the left side until the duplicate is gone.
Then add the current character to the window.
Keep updating maxLength with the longest window size found.

Time Complexity: O(n^2)
- Checking `in array` and using `pop(0)` can take O(n).

Space Complexity: O(n)
- The window can store characters from the string.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        array = []
        maxLength = 0

        for i in range(len(s)):
            while s[i] in array:
                array.pop(0)

            array.append(s[i])
            maxLength = max(maxLength, len(array))

        return maxLength