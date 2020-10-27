from functools import reduce


def base():
    add = lambda a, b: a + b
    print(add(1, 2))
    print((lambda a, b: a + b)(1, 2))


def func():
    arr = [1, 2, 3, 4, 5, 6]
    print(list(filter(lambda e: e % 3 == 0, arr)))
    print(list(map(lambda x: x * 3, range(0, 3))))
    d = [('a', 2), ('b', 3), ('c', 1), ('d', 4)]
    # [('c', 1), ('a', 2), ('b', 3), ('d', 4)] 默认正序，reverse=True倒序
    print(sorted(d, key=lambda x: x[1], reverse=True))
    # [('a', 2), ('b', 3), ('c', 1), ('d', 4)]
    print(d)
    # 两个列表元素的和
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    print(list(map(lambda x, y: x + y, a, b)))
    print(reduce(lambda x, y: '{},{}'.format(x, y), ('1', '2', '3')))


if __name__ == '__main__':
    base()
    func()
