# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # !important: deal unnecessary input
        if head == None or head.next == None:
            return head
        n = 0
        t = head
        # Tried 1: LinkList Traverse error
        while(t):
            n += 1
            t = t.next
        k %= n

        if k == 0:
            return head

        p_fast = p_slow = head
        # Tried 2: unfamiliar with python type traverse
        for i in range(k):
            p_fast = p_fast.next

        while(p_fast.next):
            p_fast = p_fast.next
            p_slow = p_slow.next

        # TIPS: Sketch could help
        p_fast.next = head
        head = p_slow.next
        p_slow.next = None
        return head


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
