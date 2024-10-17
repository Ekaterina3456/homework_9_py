# В программировании иногда возникает ситуация, когда работу функции нужно
# замедлить. Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.
from time import sleep


def wait_a_second(func):
    def wrapper(*args, **kwargs):
        print('ожидание')
        sleep(8)
        result = func(*args, **kwargs)
        return result
    return wrapper


@wait_a_second
def test():
    print("страница загружена")


if __name__ == '__main__':
    test()