def base():
    it = iter(range(0, 5))
    print(next(it))
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    # print(next(it))


# 迭代器的定义：含有__iter__()方法和__next__()方法的就是迭代器,即（iterate）
# 含有__iter__()方法就可以使用for循环，即iterable（可迭代的）
# 使用迭代方法的好处：1.可节省内存空间, 2.会从容器里面挨个取值，直到取完为止
if __name__ == '__main__':
    base()
