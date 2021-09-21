#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
# Tags: [dynamic-programming]

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(x) = f(x-1) + f(x-2)
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]
# @lc code=end
