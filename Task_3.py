# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
from functools import wraps
from typing import Callable


def counter(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{wrapper.count = }')
        return result
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('hello')


@counter
def test2():
    print('hellllooo')


if __name__ == '__main__':
    test()
    test2()