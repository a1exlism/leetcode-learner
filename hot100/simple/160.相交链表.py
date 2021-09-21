#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
# tags: [linked-list]

# @lc code=start
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            b = b.next if b else headA
        return a

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        h1, h2 = headA, headB
        l1 = l2 = 0
        while(h1):
            l1 += 1
            h1 = h1.next
        while(h2):
            l2 += 1
            h2 = h2.next
        if l1 < l2:
            h3, h4 = headB, headA
        else:
            h3, h4 = headA, headB
        for i in range(abs(l1-l2)):
            h3 = h3.next
        while(h3):
            if h3 == h4:
                return h3
            h3, h4 = h3.next, h4.next
        return None

# @lc code=end
