## 78. Subsets

Link: https://leetcode.com/problems/subsets/submissions
complexity: medium

### Solution 1:
It is pretty intuitive to write a recursive solution and reduce the task to a smaller one (DP), however it will take redundant stack memory.

Also there is no point in it, as the recursion has only one branch (tail recursion), so it is better to rewrite it iteratively.

Complexity: O(n * 2 ^ n) \
Let's count operations: n * (1 + 2 + ... + 2^(n - 1)) = n * 2 ^ n \
The same is about memory to keep intermidiate results: O(n * 2 ^ n)


### Solution 2 (backtracking):

TODO

tags:

- Recursion
- Dynamic programming
- Backtracking