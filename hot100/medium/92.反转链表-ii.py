#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
# Tags:[linked-list]
# HARD

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # left/right: position
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """ 头插法 """
        fi = ListNode(-1)
        fi.next = head
        pre = fi
        # `fixed` pre-node & cur-node
        for _ in range(left-1):
            pre = pre.next
        # insert
        cur = pre.next
        for _ in range(right-left):
            post = cur.next
            cur.next = post.next

            post.next = pre.next  # !!!
            pre.next = post

        return fi.next

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        """ 直观想法 """
        def reverse(head: ListNode):
            pre, cur = None, head
            while cur:
                post = cur.next
                cur.next = pre
                pre, cur = cur, post
            return pre
        # condition: 一开始就反转
        # 1. save origin previous head
        fi = ListNode(-1)
        fi.next = head
        pre = fi
        # 2. reversed left
        for _ in range(left-1):
            pre = pre.next
        rev_l = pre.next
        # 3. reversed right
        rev_r = rev_l
        for _ in range(right-left):
            rev_r = rev_r.next
        con_post = rev_r.next
        # 4. reverse
        rev_r.next = None
        reverse(rev_l)  # return rev_r
        # 5. re-connect
        pre.next = rev_r
        rev_l.next = con_post

        return fi.next
# @lc code=end


"""
[1,2,3,4,5], 2, 4
    p  cur
    p     cur
    p        cur
    1->2->3->4->5
    1->3->2->4->5
    1->4->3->2->5
"""
