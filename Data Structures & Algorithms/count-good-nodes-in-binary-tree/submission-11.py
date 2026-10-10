# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0

        q = deque()
        q.append((root, float("-inf")))
        count = 0

        while q:
            node, currMax = q.popleft()
            if node.val >= currMax:
                count += 1
            newMax = max(node.val, currMax)
            if node.left:
                q.append((node.left, newMax))
            if node.right:
                q.append((node.right, newMax))

        return count