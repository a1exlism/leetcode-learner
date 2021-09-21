#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
# Tags: [tree | depth-first-search | breadth-first-search]

# @lc code=start
# Definition for a binary tree node.
# Tags: [tree | depth-first-search | breadth-first-search | two-pointers]

# TIPS: dynamic lang attention
# not 0 == True; not None == True
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        # DFS 递归
        def dfs(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        # BFS 迭代
        if not root or not (root.left or root.right):
            return True  # [] or [a]
        lvl = [root.left, root.right]
        while lvl:
            l = lvl.pop(0)
            r = lvl.pop(0)
            # if l is None and r is None:
            if not (l or r):
                continue
            # if (l is None or r is None) and not (l and r):
            if not (l and r):
                # 其中一个为 None;
                return False
            if l.val != r.val:
                return False
            lvl.append(l.left)
            lvl.append(r.right)

            lvl.append(l.right)
            lvl.append(r.left)
        return True


# @lc code=end
