#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
# Tags: [string | dynamic-programming]

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        sl = len(s)
        num = 0
        for i in range(2*sl-1):  # center
            l = int(i/2)
            r = int(i/2 + i % 2)  # odd & even center
            while (l > -1 and r < sl and s[l] == s[r]):
                l -= 1
                r += 1
                num += 1
        return num


# @lc code=end
