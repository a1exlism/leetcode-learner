#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
# Tags: [linked-list | two-pointers]

# O(1) 空间需要 reverse listnode

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ 栈 & 快慢指针: 画图 """
        fp = sp = head
        stack = []
        while fp.next and fp.next.next:
            stack.append(sp.val)
            sp = sp.next
            fp = fp.next.next
        if fp.next:  # even count
            stack.append(sp.val)

        hp = sp.next  # half pointer `next`
        while hp:
            if stack.pop() != hp.val:
                return False
            hp = hp.next
        return True

    def isPalindromeSimple(self, head: ListNode) -> bool:
        """ 转数组 """
        ass = []
        h = head
        while h:
            ass.append(h.val)
            h = h.next
        i, j = 0, len(ass)-1
        while i < j:
            if ass[i] != ass[j]:
                return False
            i += 1
            j -= 1
        return True
# @lc code=end
