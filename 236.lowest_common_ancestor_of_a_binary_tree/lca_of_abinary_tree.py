# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.numDescendants(root, p, q)
        return self.ans

    def numDescendants(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if node is None:
            return 0

        leftNum = self.numDescendants(node.left, p, q)
        rightNum = self.numDescendants(node.right, p, q)
        nodeNum = int(node == p or node == q)

        if self.ans is None and leftNum + rightNum + nodeNum == 2:
            self.ans = node

        return leftNum + rightNum + nodeNum