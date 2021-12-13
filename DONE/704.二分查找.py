#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
# Tags:[]
from typing import List

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        found = -1
        while l <= r:  # = : odd size
            m = (l+r)//2
            # print(m)
            if nums[m] == target:
                found = m
                break
            elif nums[m] > target:  # too big
                r = m-1
            else:
                l = m+1
        return found


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12, 18]
    target = 9
    output = s.search(nums, target)
    print(output)
