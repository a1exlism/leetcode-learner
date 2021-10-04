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
        pre, cur = None, head  # dummy head
        while cur:
            post = cur.next
            cur.next = pre  # reverse-link
            pre, cur = cur, post  # shift
        print(post)
        return pre

    # https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-shuang-zhi-zhen-di-gui-yao-mo-/
    def reverseList2(self, head: ListNode) -> ListNode:
        # up -> down
        if not head or head.next == None:
            return head
        last = self.reverseList2(head.next)
        # down -> up; exchange
        head.next.next = head
        head.next = None
        return last
# @lc code=end
