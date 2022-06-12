### 46. Permutations

Link: https://leetcode.com/problems/permutations

Complexity: medium

Solution: \
Backtracking (we consequently expand our partial solution)

Complexity: \
Let f(N) be a number of operations needed for an array of length N. \
Thus, f(N) = N * (2 + f(N - 1)) => f(N) = 2 * (N + N(N - 1) + ... + N!) <= 2 * N * N!
Therefore, we get O(N * N!) complexity.

Memory: \
O(N!) for the solution and O(N) for recursion stack.

Tags:
- backtracking
