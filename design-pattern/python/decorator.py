from functools import wraps
import timeit


def repeat_helper(times=100):
    """ 重复使用测试函数并测试时间 """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()
            for i in range(0, times):
                fn(*args, **kwargs)
            end = timeit.default_timer()
            print(
                f'\t{fn.__qualname__} one round used {(end - start) / times * 1000:.3f} ms')

        return wrapper

    return decorator


def singleton(cls):
    """单例类装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    pass
