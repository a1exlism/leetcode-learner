from typing import List


class LinkList():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

# def exchange2(h1: LinkList, h2: LinkList):
#     h1.next = h2.next
#     h2.next = h1


class Solution():
    def exc(self, head: LinkList) -> LinkList:
        if (head.next == None or head.next.next == None):
            return head
        h1 = head.next
        h2 = head.next
        while(h1 != None and h2 != None):
            # exchange
            h1.next = h2.next
            h2.next = h1
        return head

    def test(self, l: List[int]):
        if len(l) == 0:
            return LinkList()
        h0 = LinkList(l[0])
        for i in range(1, len(l)):
            h_new = LinkList()
