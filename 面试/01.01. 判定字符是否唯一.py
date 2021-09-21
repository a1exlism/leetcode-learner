"""
https://leetcode-cn.com/problems/is-unique-lcci/

实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

tag: [bitwise | hash-table | string | sorting]

"""


class Solution:
    # hashset
    def isUnique(self, astr: str) -> bool:
        s = set(astr)
        if len(s) < len(astr):
            return False
        return True

    # space O(0)
    # bitwise: add extra long long
    def isUniqueAdv(astr: str) -> bool:
        marker = 0
        for c in astr:
            mov = ord(c) - ord('a')
            if (marker >> mov & 0b1) == 1:
                return False
            marker |= (1 << mov)
            # print(marker)
        return True
