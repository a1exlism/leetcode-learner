#
# @lc app=leetcode.cn id=?? lang=python3
#
# [62] 圆圈中最后剩下的数字
# Tags: [recurrence | math | dynamic-programming]
from random import randint


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # dp[1] = 0
        # 状态方程: dp[i] -- (m, i)
        x = 0
        for i in range(2, n+1):
            # %n, %n-1 ... %2; 删除数量一样, 剩余数唯一, ind 不同
            x = (m+x) % i

        return x

    def lastRemaining2(self, n: int, m: int) -> int:
        # 模拟删除, 超时
        l = [i for i in range(n)]
        pre = 0
        while len(l) > 1:
            # every pop
            ll = len(l)
            pre = (pre + m - 1) % ll
            l.pop(pre)
        return l[0]


if __name__ == "__main__":
    s = Solution()
    for _ in range(10):
        a, b = randint(1, 10000), randint(1, 99110)
        o1 = s.lastRemaining(a, b)
        o2 = s.lastRemaining2(a, b)
        print(f'n: {a}, m: {b}, res: {o1}')
        if o1 != o2:
            print('==ERROR==')
            break
