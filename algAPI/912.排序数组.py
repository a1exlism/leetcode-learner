#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
# Tags:[binary-search | random | divide]
from typing import List
from random import randint
# @lc code=start


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ quick sort; UNSTABLE """

        def qs(arr: List[int], l, r):
            if l >= r:
                return
            mid = partition(arr, l, r)
            qs(arr, l, mid-1)
            qs(arr, mid+1, r)
            return arr

        def partition(arr: List[int], l, r):
            # randomize pivot
            rpi = randint(l, r)
            swap(arr, l, rpi)

            middle = arr[l]
            i = l+1
            while i <= r:
                if arr[i] <= middle:
                    i += 1
                else:
                    swap(arr, i, r)
                    r -= 1
            mid = i-1
            swap(arr, l, mid)
            return mid

        qs(nums, 0, len(nums)-1)
        return nums

    def sortArray2(self, nums: List[int]) -> List[int]:
        """ merge sort | two pointers
            先分后治; divide and sort; STABLE """
        def ms(arr: List[int], l, r):
            if l >= r:
                return
            mid = (l+r) // 2  # even
            ms(arr, l, mid)
            ms(arr, mid+1, r)
            tmp = []
            a, b = l, mid+1
            while a <= mid and b <= r:  # two-pointers merge
                va, vb = arr[a], arr[b]
                if va < vb:
                    tmp.append(va)
                    a += 1
                else:
                    tmp.append(vb)
                    b += 1
            arr[l: r+1] = tmp + arr[a:mid+1] + arr[b: r+1]  # left slice

        ms(nums, 0, len(nums)-1)
        return nums

    def sortArray3(self, nums: List[int]) -> List[int]:
        """ bubble sort; STABLE """
        def bubble(arr):
            _len = len(arr)
            for i in range(0, _len-1):  # bubble n-1
                for j in range(0, _len-1-i):
                    if arr[j] > arr[j+1]:
                        swap(arr, j, j+1)
        bubble(nums)
        return nums


if __name__ == "__main__":
    s = Solution()
    data = [5, 2, 3, 6, 4, 1, 2, 1]  # [5,1,1,2,0,0]
    output = s.sortArray3(data)
    print(output)
