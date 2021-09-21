#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
# Tags: [stack | design]

# @lc code=start


class MinStack:
    """ min_diff 栈: 存与`上一个`最小值的差值
        min: 最小值
        辅助栈记忆化
    @refer https://leetcode-cn.com/problems/min-stack/solution/chai-zhi-fa-155-zui-xiao-zhan-by-fe-lucifer/
    """

    def __init__(self):
        self.min_diff = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.min_diff.append(val - self.min)  # 1
        self.min = min(self.min, val)  # 2

    def pop(self) -> None:
        diff = self.min_diff.pop()
        if diff < 0:  # pop a min val
            self.min = self.min - diff

    def top(self) -> int:
        v = self.min_diff[-1]
        return self.min if v < 0 else self.min+v

    def getMin(self) -> int:
        return self.min


class MinStack2:
    """ 辅助栈 """

    def __init__(self):
        self.stack = []
        self.min = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
# @lc code=end
