#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
# Tags: [dynamic-programming | bit-manipulation]

from typing import List
# @lc code=start
import re


class Solution:
    # @refer: https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/
    # 奇数/偶数; 递推式
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            if i % 2 == 1:
                ans.append(ans[i] + 1)
            else:
                ans.append(ans[i >> 1])

    def countBitsRE(self, n: int) -> List[int]:
        ans = []
        for x in range(n):
            ans.append(bin(x).count('1'))
            # ans.append(len(re.findall(r'1', bin(x))))
        return ans
# @lc code=end
