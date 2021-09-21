# 912. 排序数组
# 给你一个整数数组 nums, 请你将该数组升序排列.
from typing import List
import random


class Solution:
    # quick sort
    def sortArray(self, nums: List[int]) -> List[int]:

        def _sort(nums: List[int], l: int, r: int):
            if l >= r:
                return
            mid = partion(nums, l, r)
            _sort(nums, l, mid-1)
            _sort(nums, mid+1, r)

        def partion(nums: List[int], l: int, r: int) -> int:
            # randomize
            r_mid = random.randint(l, r)
            nums[r_mid], nums[l] = nums[l], nums[r_mid]

            middle = nums[l]
            lg = r
            i = l+1
            while(i <= lg):  # UNKNOWN lg value, so `=`
                if nums[i] > middle:
                    nums[i], nums[lg] = nums[lg], nums[i]
                    lg -= 1
                else:  # ELSE pass
                    i += 1
            i -= 1
            nums[l], nums[i] = nums[i], nums[l]
            # print(i, nums)
            return i

        _sort(nums, 0, len(nums)-1)
        return nums


if __name__ == '__main__':
    s = Solution()
    l = [c for c in '53723879348045684']
    nl = s.sortArray(l)
    print(nl)
