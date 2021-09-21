#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
# tags: [linked-list | two-pointers]

# @lc code=start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # !important: deal unnecessary input
        if head == None or head.next == None:
            return head
        n = 0  # len
        t = head
        while(t):
            n += 1
            t = t.next
        k %= n

        if k == 0:
            return head

        p_fast = p_slow = head  # two-point
        for i in range(k):
            p_fast = p_fast.next

        while(p_fast.next):
            p_fast = p_fast.next
            p_slow = p_slow.next

        p_fast.next = head  # shifted head
        head = p_slow.next
        p_slow.next = None
        return head

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    h = ListNode(0)
    t = h
    for i in range(3):
        l = ListNode(val=i)
        t.next = l
        t = l
    s.rotateRight(h, 2)
    s.rotateRight(None, 0)
