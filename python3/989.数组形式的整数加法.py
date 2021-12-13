#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
# Difficulty:[easy->HARD]

from typing import List

# @lc code=start


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num)-1
        c = 0
        while i > -1:
            print(i)
            s = num[i] + k % 10 + c
            num[i] = s % 10
            c = s / 10
            k /= 10
            i -= 1
        k += c
        while k:
            num.insert(0, k % 10)
            k /= 10
        return num

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 0, 0]
    K = 34
    out = s.addToArrayForm(A, K)
    print(out)
