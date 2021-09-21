#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
# Tags: [linked-list | two-pointers]
# hashset 可以直接解

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
快慢指针; 若循环则总能找到交点
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fp = sp = head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                return True
        return False

# @lc code=end
