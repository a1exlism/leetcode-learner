class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        TIPS: stack out get a same order with queue
        """
        self.stackIn.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stackOut) == 0:
            while(len(self.stackIn) > 0):
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()

    def peek(self) -> int:
        """
        Get the front element.
        BETTER: code reuse
        """
        res = self.pop()
        self.stackOut.append(res)
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stackIn) + len(self.stackOut) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
