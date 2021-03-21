"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        # DFS
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        return 0

    def maxDepth2(self, root: TreeNode) -> int:
        # BFS
        if not root:
            return 0
        queue = [root]
        depth = 1
        while(queue):
            level = queue[:]
            queue.clear()
            depth += 1
            while(level):
                t = level.pop(0)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)

        return depth