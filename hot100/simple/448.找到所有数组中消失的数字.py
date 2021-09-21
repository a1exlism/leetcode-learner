#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
# Tags: [array]
from typing import List
# @lc code=start


class Solution:
    """
        input range: [1,n]
        数组本身作为 hashset
        出现过的 index 做标记
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for x in nums:
            ind = (x-1) % n  # multiple addition
            nums[ind] += n
        for i, x in enumerate(nums):
            if x <= n:
                res.append(i+1)
        return res

    """ hashset, extra space """

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []
        for x in range(1, len(nums)+1):
            if x not in s:
                res.append(x)
        return res

# @lc code=end
