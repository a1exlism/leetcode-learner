# refer https://refactoringguru.cn/design-patterns/singleton/python/example#example-1
from typing import Any
from threading import Lock, Thread


class SingletonMeta(type):
    # 元类 实现
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                # create instance
                instance = super().__call__(*args, **kwds)
                # refer instance
                cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def business_logic(self):
        print('BUSINESS LOGIC...')


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()

# if __name__ == "__main__":
#     s1 = Singleton()
#     s2 = Singleton()

#     print(s1 == s2)
#     print(s1)
#     print(id(s1))
