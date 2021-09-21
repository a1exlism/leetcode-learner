#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
# Tags: [hash-table | stack | tree]

from typing import List
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ recurrence """
        def inorder(r: TreeNode, arr: list):
            if not r:
                return
            inorder(r.left, arr)
            arr.append(r.val)
            inorder(r.right, arr)

        res = []
        inorder(root, res)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """ iteration & stack; 模拟递归栈 """
        p = root
        res, stack = [], []
        while not p or stack:
            while p:
                stack.append(p)
                p = p.left
            # until left is None
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res

    def inorderTraversalMorris(self, root: TreeNode) -> List[int]:
        """ Morris linklist; """
        res = []
        predecessor = None  # mostRight 节点
        p = root
        while p:
            if not p.left:  # 如果没有左孩子，则直接访问右孩子
                res.append(p.val)
                p = p.right
            else:
                # predecessor 节点就是当前 root 节点向左走一步，然后一直向右走至无法走为止
                predecessor = p.left
                while predecessor.right and predecessor.right != p:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # 让 predecessor 的右指针指向 root，继续遍历左子树
                    predecessor.right = p
                    p = p.left
                else:
                    # 左子树已经访问完了，我们需要断开链接
                    res.append(p.val)

                    predecessor.right = None
                    p = p.right
        return res


# @lc code=end
