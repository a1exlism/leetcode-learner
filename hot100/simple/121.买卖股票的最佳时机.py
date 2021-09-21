#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
# Tags: [array | dynamic-programming]
# 思路比较重要: min in previous; max profit = now - min

from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        lp = len(prices)
        minprice = float('inf')
        for i in range(lp):
            mp = max(mp, prices[i]-minprice)
            minprice = min(prices[i], minprice)
        return mp
# @lc code=end
