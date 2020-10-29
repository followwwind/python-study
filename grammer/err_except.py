# 抓捕异常
def try_except():
    try:
        3 / 0
    except ZeroDivisionError as err:
        print("zero error: {0}".format(err))
    finally:
        print("this is finally")
    print("try_except")


# 抛出异常
def raise_study():
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
    # 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise


# 自定义异常
def self_exception():
    try:
        raise MyError(2 * 2)
    except MyError as e:
        print('My exception occurred, value:', e.value)


# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    # try_except()
    # raise_study()
    self_exception()
