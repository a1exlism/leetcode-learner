#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
# Tags: [tree | breadth-first-search]

from typing import List
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level_size = len(queue)
            res.append([])
            for _ in range(level_size):
                p = queue.pop(0)
                res[-1].append(p.val)
                l, r = p.left, p.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)
        return res

# @lc code=end
