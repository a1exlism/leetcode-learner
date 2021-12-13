# refer https://refactoringguru.cn/design-patterns/singleton/python/example#example-1
from typing import Any
from threading import Lock, Thread


class Singleton():
    def __new__(cls, *arg, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *arg, **kw)
        return cls._instance


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 == s2)
    print(s1)
    print(id(s1))
