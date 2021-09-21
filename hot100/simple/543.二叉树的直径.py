#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
# Tags: [tree]

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth = -1

        def dfs(p):
            if not p:
                return 0
            l = dfs(p.left)
            r = dfs(p.right)
            self.depth = max(self.depth, l+r+1)
            return max(l, r) + 1
        dfs(root)
        return self.depth - 1  # len=节点个数-1
# @lc code=end
