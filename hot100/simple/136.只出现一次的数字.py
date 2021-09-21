#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
# Tags: [hash-table | bit-manipulation]
# TIPS: a ^ a = 0; a ^ 0 = a

from typing import List
from functools import reduce
# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber2(self, nums: List[int]) -> int:
        # extra space cost: O(n)
        s = set()
        for x in nums:
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        return s.pop()
# @lc code=end
