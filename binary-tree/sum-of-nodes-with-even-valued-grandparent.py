# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_even_valued):
            if not node:
                return 0
            res = dfs(node.left, node.val % 2 == 0) + dfs(node.right, node.val % 2 == 0)
            if is_even_valued:
                if node.left:  res += node.left.val
                if node.right: res += node.right.val
            return res            
        return dfs(root, False)        