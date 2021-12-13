#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
# Tags: [math | string]
# Difficulty:[medium]
# Companies: [Bytedance]
# 思路: 提前分好内存, 按位计算和进位;

# @lc code=start
class Solution:
    """ 进位不会连续进两次(结果所证), 所以简单 """

    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1+l2)
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                v = res[i+j+1] + int(num1[i]) * int(num2[j])
                # print(v)
                res[i+j+1] = v % 10  # low bit
                res[i+j] += v // 10  # high bit
        # prefix
        i = 0
        while i < len(res)-1 and res[i] == 0:
            i += 1
        return ''.join([str(v) for v in res[i:]])

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # a = '0'
    # b = '0'
    a = '123'
    # a = '999'
    b = '456'
    # b = '999'
    output1 = s.multiply(a, b)
    print(output1)
