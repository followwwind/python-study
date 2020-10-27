from math import pi, ceil, sin, degrees
from random import random, choice


def base():
    print(int("3"))
    # 3
    print(int(3.14))
    print(float(3))
    # 整数除法返回浮点型
    print(6/3)
    print(type(6/3))
    print(isinstance(6/3, float))
    print(2 ** 3)
    print(complex(3, 4))


def func():
    print(pi)
    print(round(3.145, 2))
    print(ceil(3.145))
    # 90.0
    print(degrees(pi/2))
    print(sin(pi/2))
    print(int(random() * 10))
    # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    print(choice(range(10)))


if __name__ == '__main__':
    base()
    func()
