#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
# Tags:[stack | design]
# Difficulty:[easy]
# @lc code=start
class MyQueue:

    def __init__(self):
        self.sin = []  # FI
        self.sout = []  # FO

    def push(self, x: int) -> None:
        self.sin.append(x)

    def pop(self) -> int:
        """ premise: number > 0 """
        if not self.sout:  # empty
            while self.sin:
                self.sout.append(self.sin.pop())
        return self.sout.pop()

    def peek(self) -> int:
        """ premise: number > 0 """
        if not self.sout:
            while self.sin:
                self.sout.append(self.sin.pop())
        return self.sout[-1]

    def empty(self) -> bool:
        return not (self.sin or self.sout)


# @lc code=end
# Your MyQueue object will be instantiated and called as such:
queue = MyQueue()
queue.push(1)  # queue is: [1]
queue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
p1 = queue.peek()  # return 1
p2 = queue.pop()  # return 1, queue is [2]
p3 = queue.empty()  # return false

print(p1, p2, p3)
