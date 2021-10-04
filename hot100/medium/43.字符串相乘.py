#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
# Tags: [math | string]
# Companies: [Bytedance]
# 思路: 提前分好内存, 按位计算和进位;

# @lc code=start
class Solution:
    """ 进位不会连续进两次(结果所证), 所以简单 """

    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = list(int(i) for i in num1), list(int(i) for i in num2)
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1+l2)
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                # print(f'i: {i} j: {j}; {num1[i]}, {num2[j]}')
                p1, p2 = i+j, i+j+1
                v = res[p2] + num1[i] * num2[j]  # new val = old low bit + mul
                res[p2] = v % 10  # low bit
                res[p1] += v // 10  # high bit
        # prefix 0
        i = 0
        while i < len(res)-1 and res[i] == 0:
            i += 1
        return ''.join(str(e) for e in res[i:])

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # a = '0'
    # b = '0'
    a = '123'
    # # a = '999'
    b = '456'
    # b = '999'
    output = s.multiply(a, b)
    print(output)
