# [3] 无重复字符的最长子串
# [hash-table | two-pointers | string | sliding-window]
# ATTENTION: 回顾

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  substring: s[l,..., r]
        slen = len(s)
        maxlen = 0
        occ = set()
        r = 0
        for l in range(slen):
            if l > 0:
                # redundant
                occ.remove(s[l-1])
            # 该重复之前的字串均已确定, 不需要管顺序
            while r < slen and s[r] not in occ:
                occ.add(s[r])
                r += 1
            maxlen = max(maxlen, r-l)  # s[r] redundant
        return maxlen
# @lc code=end
