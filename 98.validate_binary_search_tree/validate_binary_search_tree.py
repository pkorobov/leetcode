# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, -float('inf'), float('inf'))

    def _isValidBST(self, node: Optional[TreeNode], cur_min: int, cur_max: int):
        if node is None:
            return True
        if node.val <= cur_min or node.val >= cur_max:
            return False
        return self._isValidBST(node.left, cur_min, node.val) and \
               self._isValidBST(node.right, node.val, cur_max)
