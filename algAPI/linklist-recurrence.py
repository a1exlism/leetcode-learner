class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


count = 0


def pind(n: int):
    for i in range(n):
        print("  ")


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
    print(res)
    return res


def fn(n: int):
    if hasattr(fn, "count"):
        fn.count += 1
    else:
        fn.count = 1
    if n == 0:
        return
    print(f'count: {fn.count}')
    fn(n-1)
    print(n)


def rec(head: ListNode):
    """ up -> down """
    if not head:
        return
    print(f'- {head.val}')
    rec(head.next)
    """ down -> up """
    print(f'= {head.val}')


def rec2(head: ListNode):
    """ 前提: head != None """
    print(f"-- {head.val}")
    if head.next == None:
        print(head.val)
        return
    rec2(head.next)
    # sth with NON-last node
    print(f"== {head.val}")
    return


def reverse_node(head: ListNode) -> ListNode:
    if not (head and head.next):
        return head
    last = reverse_node(head.next)

    # exchange
    head.next.next = head
    head.next = None

    return last


if __name__ == "__main__":
    p = gen_ll([1, 2, 3, 4])
    rec(p)
    # print(p.next.val)
    rec2(p)  # [9]*5
    p = reverse_node(p)
    print_ll(p)
