#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
# Tags:[linked-list]

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        while head.val != left:
            head = head.next

        def recr(pre: ListNode, target: int):
            if pre.val == target:
                return pre
            pre.next = recr(pre.next)


# @lc code=end
