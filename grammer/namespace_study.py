num = 1
name = 'wind'


def fun_global():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer():
    i = 10

    def inner():
        nonlocal i   # nonlocal关键字声明
        i = 100
        print(i)
    inner()
    print(i)


# 一般有三种命名空间：
# （built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
# 命名空间查找顺序: 局部的命名空间去 -> 全局命名空间 -> 内置命名空间
if __name__ == '__main__':
    fun_global()
    print(num)
    outer()
