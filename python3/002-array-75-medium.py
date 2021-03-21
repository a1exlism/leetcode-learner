from typing import List
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        p1: 0
        p2: 2
        i: last 1
        """
        p1, p2 = 0, len(nums)-1
        i = 0
        # TIPS: p2+1
        while(i < p2+1):
            v = nums[i]
            if v == 0:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif v == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
                # ATTENTION: all 3 letters
                if v != 1:
                    i -= 1
            i += 1


if __name__ == "__main__":
    s = Solution()
    # l = [2, 0, 2, 1, 1, 0]
    l = [1, 2, 0]
    s.sortColors(l)
    print(l)
