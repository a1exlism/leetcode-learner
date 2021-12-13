#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
# Difficulty:[easy]
from typing import List

# @lc code=start


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        prev = float('inf')
        # L -> R
        for i, v in enumerate(s):
            if v == c:
                prev = i
            ans.append(abs(i-prev))
        # R -> L; index: big -> small
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], abs(prev-i))
        return ans

    def shortestToCharTrivial(self, s: str, c: str) -> List[int]:
        carr = []
        ans = [10000] * len(s)
        for i, v in enumerate(s):
            if v == c:
                carr.append(i)
                ans[i] = 0
        for ie in carr:
            for i in range(0, len(s)):
                ans[i] = min(ans[i], abs(ie-i))
        return ans


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ss = "aaab"
    cc = "b"
    output = s.shortestToChar(ss, cc)
    print(output)
