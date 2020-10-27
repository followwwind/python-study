# 关键字参数
def func(name, age):
    print(f"name is {name}, age is {age}")


# 默认参数
def func2(name, age=21):
    print(f"name is {name}, age is {age}")


# 不定长参数, 元组
def func3(name, *args):
    print(f"name is {name}, args is {args}")


# 不定长参数, 字典
def func4(name, **d):
    print(f"name is {name}, d is {d}")


# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
def func5(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


if __name__ == '__main__':
    # 使用关键字参数允许函数调用时参数的顺序与声明时不一致
    func(age=18, name='wind')
    func2('cici')
    func3(1, 2, 3)
    func4(1, username='wind', age=27)
    func5(10, 20, 30, d=40, e=50, f=60)
else:
    print("__name__ hello import")
