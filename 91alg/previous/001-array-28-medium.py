# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

class Solution:
    # Basic Sliding Window
    def strStrBSW(self, text: str, pat: str) -> int:
        lt, lp = len(text), len(pat)
        if not pat:
            return 0
        if lt < lp:
            return -1
        for start in range(lt-lp+1):  # same as: n-1+1
            if text[start:start+lp] == pat:
                return start
        return -1

    # double pointer Sliding Window Optimize
    def strStr(self, text: str, pat: str) -> int:
        lt, lp = len(text), len(pat)
        if not pat:
            return 0
        if lt < lp:
            return -1
        for i in range(0, lt-lp+1):
            # extend window break rule
            for j in range(0, lp):
                if text[i+j] != pat[j]:
                    break
                if j == lp-1:
                    return i
        return -1

    # Karbin Karp


if __name__ == '__main__':
    str = Solution().strStr
    res = str("bcbcbcbcbea", "bcbcbea")  # 11, 7
    print(res)
