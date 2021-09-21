#
# TIPS: python is DIFFERENT
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
# Tags: [bit-manipulation]
# 剑指 offer65
# @refer: https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/

"""
bitwise:
a b sum
0 0 00
0 1 01
1 0 01
1 1 10
carry = a & b
sum(local) = a ^ b
"""

# @lc code=start


class Solution:
    def getSum(self, a: int, b: int) -> int:
        p = 0xffffffff  # 32 bit unsigned
        a &= p
        b &= p
        while b != 0:
            # sum(local) , carry(next)
            a, b = a ^ b, (a & b) << 1 & p
        if a <= 0x7fffffff:
            return a
        else:  # 还原实际值 (python 没有直接补码)
            return ~(a ^ p)
# @lc code=end
