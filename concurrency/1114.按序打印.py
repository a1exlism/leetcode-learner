#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
# Difficulty:[easy]
# Tags:[concurrency]

from threading import Lock
# @lc code=start


class Foo:
    """ https://docs.python.org/zh-cn/3/library/threading.html """

    def __init__(self):
        self.first_job_done = Lock()
        self.second_job_done = Lock()
        self.first_job_done.acquire()  # lock
        self.second_job_done.acquire()  # lock

    def first(self, printFirst: 'Callable[[], None]') -> None:

        printFirst()
        self.first_job_done.release()  # unlock

    def second(self, printSecond: 'Callable[[], None]') -> None:

        if self.first_job_done.acquire():  # same as with
            printSecond()
        self.second_job_done.release()  # unlock

    def third(self, printThird: 'Callable[[], None]') -> None:

        with self.second_job_done:
            printThird()
# @lc code=end
