#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
# Tags: [bit-manipulation]

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = min(x, y), max(x, y)
        res = 0
        while y > 0:  # check bit by bit
            if (y & 0b1) ^ (x & 0b1) == 1:
                res += 1
            x >>= 1
            y >>= 1
        return res

    def hammingDistanceQuick(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

# @lc code=end
