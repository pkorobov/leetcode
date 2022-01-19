## 236. Lowest Common Ancestor of a Binary Tree

Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Complexity: medium

Solution: \
Count occurences of p and q nodes in the tree while traversing it.
The first node in which two nodes are visited is the desired one.

Complexity: O(n), as we traverse the tree only once

Memory: O(h), where h is the height of the tree

tags:
- dfs
- trees
- graphs
- lca
