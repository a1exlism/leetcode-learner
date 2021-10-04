#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
# 最优时间复杂度: O(rowIndex) 关于数学函数, 做题不参考
# Tags:[array]
from typing import List

# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """ O(rind^2)"""
        row = [1]
        ind = 1
        while ind < rowIndex+1:
            row = [1] + [row[i-1]+row[i] for i in range(1, len(row))] + [1]
            ind += 1
        return row

    def getRow2(self, rowIndex: int) -> List[int]:
        """ 当前行第 i 项的计算只与上一行第 i−1 项及第 i 项有关
            => 倒序 保存上一行结果 (i-1)
        """
        row = [1] + [0] * (rowIndex)
        for rn in range(1, rowIndex+1):  # row num
            for j in range(rn, 0, -1):
                row[j] += row[j-1]
        return row

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    data = 3
    output = s.getRow2(data)
    print(output)
