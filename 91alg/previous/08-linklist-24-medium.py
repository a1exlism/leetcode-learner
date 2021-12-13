# 两两交换链表中的节点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def _print(self):
        t = self
        arr = []
        while(t):
            arr.append(t.val)
            t = t.next
        print(arr)
        return arr


class Solution:
    # Recurrence
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        r = head.next
        head.next = self.swapPairs(r.next)
        r.next = head
        return r

    # iteration advanced
    # iterate by every two step
    def swapPairs(self, head: ListNode) -> ListNode:
        f_head = ListNode(next=head)
        l = head
        pre = f_head
        while(l and l.next):
            r = l.next
            l.next = r.next
            r.next = l
            pre.next = r
            pre = l
            l = l.next
        return f_head.next


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 4]
    # arr = [1, 2, 3]
    # arr = [1, 2]
    h, pre = None, None
    for i, v in enumerate(arr):
        now = ListNode(v)
        if i == 0:
            pre = ListNode(v)
            h = pre  # head
        else:
            pre.next = now
            pre = now
    h._print()
    h = s.swapPairs(h)
    h._print()
