# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове с теми же аргументами,
# возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
# если такие аргументы уже использовались, должен вернуть сохранённый результат
# вместо запуска расчёта.
from typing import Callable


def cash(func: Callable):
    data = []
    def wrapper(num, *args, **kwargs):
        result = func(num, *args, **kwargs)
        data.append(result)
        return data
    return wrapper


@cash
def fibbo(num):
    fibbo1 = 0
    fibbo2 = 1
    fibbonachi = [fibbo1, fibbo2]
    for _ in range(num-2):
        if fibbo1 < fibbo2:
            fibbo1 = fibbo1 + fibbo2
            fibbonachi.append(fibbo1)
        else:
            fibbo2 = fibbo2 + fibbo1
            fibbonachi.append(fibbo2)
    return fibbonachi


if __name__ == '__main__':
    print(fibbo(5))
    print(fibbo(5))
    print(fibbo(8))
