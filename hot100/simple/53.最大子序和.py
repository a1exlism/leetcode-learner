#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
# Tags: [array | divide-and-conquer | dynamic-programming]


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = sum = float('-inf')
        for x in nums:
            sum = max(sum+x, x)
            res = max(res, sum)
        return res
# @lc code=end
