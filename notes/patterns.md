# Algorithm Patterns

This file summarizes common algorithm patterns from Blind 75.

---

## 1. Arrays & Hashing

Use this pattern when you need to quickly check if something exists, count values, or store previous results.

Common tools:
- Hash map / dictionary
- Hash set
- Frequency count

Example problems:
- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams

Main idea:
Instead of checking every pair one by one, store useful information in a dictionary or set so we can look it up quickly.

---

## 2. Two Pointers

Use this pattern when you can solve the problem by moving two indexes.

Common tools:
- Left pointer
- Right pointer
- Sorted array logic

Example problems:
- Container With Most Water
- 3Sum

Main idea:
Start with two pointers and move one of them based on the condition.

---

## 3. Sliding Window

Use this pattern when the problem asks about a subarray or substring.

Common tools:
- Left pointer
- Right pointer
- Current window
- Hash map / frequency count

Example problems:
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Best Time to Buy and Sell Stock

Main idea:
Expand the right side of the window, and shrink the left side when the window becomes invalid.

---

## 4. Stack

Use this pattern when the most recent item matters first.

Common tools:
- Stack list
- Push
- Pop

Example problems:
- Valid Parentheses

Main idea:
The last thing added is the first thing removed.

---

## 5. Binary Search

Use this pattern when the answer can be found by cutting the search space in half.

Common tools:
- left
- right
- mid

Example problems:
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

Main idea:
Compare the middle value with the target or condition, then remove half of the search space.

---

## 6. Linked List

Use this pattern when nodes are connected by `next`.

Common tools:
- Dummy node
- Fast and slow pointers
- Previous pointer
- Current pointer

Example problems:
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Reorder List

Main idea:
Instead of using indexes, move through nodes using pointers.

---

## 7. Trees

Use this pattern when each node can have children.

Common tools:
- DFS
- BFS
- Recursion
- Queue

Example problems:
- Invert Binary Tree
- Maximum Depth of Binary Tree
- Same Tree
- Validate Binary Search Tree

Main idea:
Visit nodes one by one using recursion or a queue.

---

## 8. Heap / Priority Queue

Use this pattern when you need the smallest or largest value quickly.

Common tools:
- Min heap
- Max heap
- Priority queue

Example problems:
- Merge K Sorted Lists
- Find Median from Data Stream
- Top K Frequent Elements

Main idea:
A heap helps us quickly get the highest-priority value.

---

## 9. Backtracking

Use this pattern when you need to try all possible choices.

Common tools:
- Choose
- Explore
- Undo

Example problems:
- Combination Sum
- Permutations
- Word Search

Main idea:
Try one choice, continue searching, and undo the choice before trying another option.

---

## 10. Graphs

Use this pattern when things are connected to each other.

Common tools:
- DFS
- BFS
- Visited set
- Adjacency list
- Topological sort
- Union Find

Example problems:
- Clone Graph
- Course Schedule
- Number of Islands
- Graph Valid Tree

Main idea:
Represent connections, then visit connected nodes carefully without repeating.

---

## 11. Dynamic Programming

Use this pattern when the problem can be broken into smaller repeated subproblems.

Common tools:
- Base case
- State
- Recurrence relation
- Memoization
- DP table

Example problems:
- Climbing Stairs
- House Robber
- Coin Change
- Word Break
- Longest Increasing Subsequence

Main idea:
Save previous results so we do not solve the same problem again.

---

## 12. Intervals

Use this pattern when the problem has start and end times or ranges.

Common tools:
- Sort by start time
- Compare current interval with previous interval

Example problems:
- Merge Intervals
- Insert Interval
- Meeting Rooms
- Meeting Rooms II

Main idea:
Sort intervals first, then check if they overlap.

---

## 13. Matrix

Use this pattern when the input is a 2D grid.

Common tools:
- Row
- Column
- Direction arrays
- Visited set

Example problems:
- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes
- Word Search

Main idea:
Move through rows and columns carefully while checking boundaries.