"""
给定一个单链表，其中的元素按升序排序，将其转换为`高度平衡`的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # TIPS-1: 快慢指针
    # TIPS-2: 递归
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def genTree(l: ListNode, r: ListNode) -> TreeNode:
            # leaf node
            if l == r:
                return None
            # get medium node
            fast = slow = l
            while(fast != r and fast.next != r):
                slow = slow.next
                fast = fast.next.next
            # gen tree by recurrence
            root = TreeNode(slow.val)
            root.left = genTree(l, slow)
            root.right = genTree(slow.next, r)
            return root

        return genTree(head, None)
