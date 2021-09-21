#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
# Tags:[tree]

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        # BFS
        if not root:
            return
        lvl = [root]
        while lvl:
            lvl_size = len(lvl)
            for _ in range(lvl_size):
                p = lvl.pop(0)
                l, r = p.left, p.right
                if l:
                    lvl.append(l)
                if r:
                    lvl.append(r)
                p.right, p.left = l, r
        return root


# @lc code=end
