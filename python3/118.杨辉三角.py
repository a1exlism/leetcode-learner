#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
# [array]
from typing import List

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ n-th row --> `n+1` numbers """
        res = [[1]]
        for n in range(1, numRows):
            pre_row = res[-1]
            row = [1]
            for i in range(1, n):
                row.append(pre_row[i-1] + pre_row[i])
            row.append(1)
            res.append(row)
        return res

    def generate2(self, numRows: int) -> List[List[int]]:
        """ recurrence """
        if numRows == 1:  # ↑↑
            return [[1]]
        res = self.generate2(numRows-1)  # ↓↓
        pre = res[-1]
        row = [1] + [pre[i-1] + pre[i] for i in range(1, len(pre))] + [1]
        res.append(row)
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    nr = 5
    output = s.generate2(nr)
    print(output)
