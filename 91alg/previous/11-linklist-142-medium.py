# Definition for singly-linked list.
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Hash table
    def detectCycle(self, head: ListNode) -> ListNode:
        h = head
        s = set()
        while(h):
            if hash(h) in s:
                return h
            else:
                s.add(hash(h))
            h = h.next
        return None

    # fast & slow
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while(True):
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while(fast != slow):
            fast = fast.next
            slow = slow.next
        return fast
