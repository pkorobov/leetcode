## 1676. Lowest Common Ancestor of a Binary Tree IV

Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

Complexity: medium

Solution: \
Traverse the tree recursively, check the current node if it is in the descendants list or set (depending on use of extra memory). \
If so, return it.
If the current node has two children from the descendants list return this node. 
If only one, then return this one. \
See the code for more clarity.

Complexity: O(n) or O(n^2) -- depends on use of hashset.

Memory: O(k) or O(1) -- depends on use of hashset.

tags:
- dfs
- trees
- graphs
- lca
