class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def gen_ll(nums: list) -> ListNode:
    if not nums:
        return None
    cur = head = ListNode(nums[0])
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def print_ll(head: ListNode) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
