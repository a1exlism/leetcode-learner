# 难度觉得是 Simple
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        if type(x) == int:
            self.stack.append(x)
        else:
            self.stack.append(None)

    def pop(self) -> int:
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        count = min(len(self.stack), k)
        for i in range(count):
            self.stack[i] += val


class CustomStackPure:
    def __init__(self, maxSize: int):
        self.stack = [0]*maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top == len(self.stack)-1:
            return
        self.top += 1
        if type(x) == int:
            self.stack[self.top] = x
        else:
            self.stack[self.top] = None

    def pop(self) -> int:
        if self.top == -1:
            return -1
        else:
            del_pos = self.top
            self.top -= 1
            return self.stack[del_pos]

    def increment(self, k: int, val: int) -> None:
        min_edge = min(k, self.top+1)
        for i in range(min_edge):
            self.stack[i] += val


# if __name__ == '__main__':
#     stack = [1, 2, 3, 4, 5]
#     val = 100
#     t = 4
#     K = 5
#     while (K > 0 and t > -1):
#         stack[t] += val
#         print(stack[t])
#         t -= 1
#         K -= 1
