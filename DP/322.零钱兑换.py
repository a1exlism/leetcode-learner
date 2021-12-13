#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
# Tags:[dynamic-programming | 完全背包]
from typing import List
from functools import lru_cache
# @lc code=start

INF = float('inf')


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ dp, 迭代 all best solution for [0, amount] """
        if amount < 0:
            return -1
        dp = [0] + [INF] * amount
        for c in coins:
            for n in range(1, amount+1):
                if n >= c:  # get minimum
                    dp[n] = min(dp[n], dp[n-c]+1)
        res = dp[amount]
        # print(dp)
        return res if res != INF else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """ recurrence 当前状态由前一个状态所得
            space: O(amount*n)
        """

        @lru_cache(amount)  # 很重要, 参考例2
        def dfs(rem):
            if rem < 0:
                return INF
            if rem == 0:
                return 0
            res = INF
            for c in coins:
                # print(c)
                res = min(res, dfs(rem - c) + 1)  # select c or Not
            return res
        res = dfs(amount)
        return -1 if res == INF else res
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    coins = [2]
    amount = 11
    coins2 = [186, 419, 83, 408]
    amount2 = 6249
    coins3 = [1]
    amount3 = -12
    output = s.coinChange(coins, amount)
    print(output)
    output = s.coinChange(coins2, amount2)
    print(output)
    output = s.coinChange(coins3, amount3)
    print(output)
