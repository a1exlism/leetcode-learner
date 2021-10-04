#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
# Tags: [string]
# Medium 一时间不太会写

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        c = 0  # bit carry
        res = ''
        while i >= 0 or j >= 0:
            v1 = int(num1[i]) if i > -1 else 0  # padding
            v2 = int(num2[j]) if j > -1 else 0  # padding
            v = v1 + v2 + c
            s = v % 10
            res = str(s) + res  # concatanation
            c = v // 10
            i, j = i-1, j-1
        return str(c) + res if c else res


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    data = ['111', '123']
    output = s.addStrings(data[0], data[1])
    print(output)
