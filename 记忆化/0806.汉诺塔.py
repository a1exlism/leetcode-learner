#
# @lc app=leetcode.cn lang=python3
""" ATTENTION: 不清楚正确性验证 """
#
# [08.16] 汉诺塔
# Tags:[array | recurrence | memo]
# Difficulty:[easy]
from typing import List
# @lc code=start


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """ 确定状态 & 转移方程
            num:  n -> n-1;
            data: [n-1]: A -> B, n-th: A -> C,
                  then [n-1]: B -> C
        """
        num = len(A)

        def mov(n, a, b, c) -> None:
            # print(n, a, b, c)
            if n == 1:
                c.append(a.pop())
                return
            mov(n-1, a, c, b)  # a -> b: n-1 stack
            c.append(a.pop())
            mov(n-1, b, a, c)  # b -> c: n-1 stack
        mov(num, A, B, C)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    A = [2, 1, 0]
    B = []
    C = []
    s.hanota(A, B, C)
    print(A, B, C)
