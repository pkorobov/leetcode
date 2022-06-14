### 46. Permutations

Link: https://leetcode.com/problems/permutations

Complexity: medium

Solution 1: \
Backtracking (we consequently expand our partial solution)

Complexity: \
Let f(N) be a number of operations needed for an array of length N. \
Thus, f(N) = N * (2 + f(N - 1)) => f(N) = 2 * (N + N(N - 1) + ... + N!) <= 2 * N * N!
Therefore, we get O(N * N!) complexity.

Memory: \
O(N!) for the solution and O(N) for recursion stack.

---

Solution 2: \

DFS-like approach 

Start from empty array for the current permutation array.
Let's mark a currently added element and pass the extended current permutation array into the next recursion step.
After the end of recursion unmark the element added before.
We add the current permutation array into answers when it's length reaches N.

Complexity: \
Let f(N) be a number of operations needed for an array of length N. \
Thus, f(N) = N * (2 + f(N - 1)) => f(N) = 2 * (N + N(N - 1) + ... + N!) <= 2 * N * N!
Therefore, we get O(N * N!) complexity.

Memory: \
O(N!) for the solution and O(N) for recursion stack.


Tags:
- backtracking, dfs
