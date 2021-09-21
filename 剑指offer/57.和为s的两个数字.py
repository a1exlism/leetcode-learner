"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[2,7] 或者 [7,2]
"""
# Tags: [two-pointer]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(set(nums))
        nums.sort()
        l, r = 0, len(nums)-1
        res = []
        while l < r:
            L = nums[l]
            R = nums[r]
            if L+R == target:
                return [L, R]
                # l += 1
            elif L+R < target:
                l += 1
            else:
                r -= 1
