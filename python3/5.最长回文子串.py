#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
# Tags: [string | dynamic-programming]
# Difficulty:[medium]


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ dp O(n2) """
        n = len(s)
        # dp[start:end+1] initial
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

    def longestPalindrome2(self, s: str) -> str:
        """ 中心扩散 O(n2) """
        def expand_check(l, r):
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1  # TIPS

        start = end = 0
        for i in range(len(s)-1):
            l1, r1 = expand_check(i, i)  # odd
            l2, r2 = expand_check(i, i+1)  # even
            if r1-l1 > end-start:
                start, end = l1, r1
            if r2-l2 > end-start:
                start, end = l2, r2
        return s[start: end+1]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    data = "babad"
    data = "ac"
    output = s.longestPalindrome(data)
    print(output)
