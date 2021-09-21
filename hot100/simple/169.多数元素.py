#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#       => 大于 ⌊ n/2 ⌋ 的元素
# Tags: [array | divide-and-conquer | bit-manipulation]

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ 投票法 Boyer-Moore ; O(n) & O(1) """
        candidate = -1
        count = 0
        for x in nums:
            if count == 0:  # next candidate
                candidate = x
            if x == candidate:
                count += 1
            else:
                count -= 1
        return candidate

    def majorityElement2(self, nums: List[int]) -> int:
        """ 排序法 """
        nums.sort()
        return nums[len(nums)//2]


# @lc code=end
