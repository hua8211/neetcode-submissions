# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val : i for i, val in enumerate(inorder)}
        self.preIdx = 0

        def dfs(lo, hi):
            if lo > hi:
                return None
            
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(lo, mid - 1)
            root.right = dfs(mid + 1, hi)

            return root

        return dfs(0, len(inorder) - 1)