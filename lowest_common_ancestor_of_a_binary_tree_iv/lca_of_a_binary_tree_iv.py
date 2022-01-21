# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', descendants: 'List[TreeNode]') -> 'TreeNode':
        # use hash table to solve for O(n)
        descendants = {node.val for node in descendants}
        lca = self._lowestCommonAncestor(root, descendants)
        return lca

    def _lowestCommonAncestor(self, node: 'TreeNode', descendants: 'Set[TreeNode]') -> 'TreeNode':
        if node is None:
            return None

        if node.val in descendants:
            # don't need to search for this node anymore
            descendants.remove(node.val)
            return node

        left = self._lowestCommonAncestor(node.left, descendants)
        right = self._lowestCommonAncestor(node.right, descendants)
        if left is not None and right is not None:
            return node
        elif left is not None:
            return left
        return right
