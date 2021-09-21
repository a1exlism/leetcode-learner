#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
# Tags: [linked-list]

# @lc code=start
# Definition for singly-linked list.
# 每个节点只考虑next即可
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        pre, cur = head, head.next
        while cur:
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        head.next = None
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        # recursion
        if not head or head.next == None:
            return head
        # traverse first
        next_head = self.reverseList2(head.next)
        # None.next ERROR
        head.next.next = head
        head.next = None
        return next_head
# @lc code=end
