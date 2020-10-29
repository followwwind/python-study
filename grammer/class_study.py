"""一个简单的类实例"""


class Person:
    # 定义基本属性
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def print_info(self):
        print(self.__weight)


# 单继承示例
class Student(Person):
    grade = 0

    def __init__(self, name):
        Person.__init__(self, name)
        # super().__init__(name)

    # 打印，转换
    def __repr__(self):
        return "student"

    # 覆写父类的方法
    def print_info(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


if __name__ == '__main__':
    p = Person('wind')
    print(p.name)
    print(p.get_name())
    p.print_info()

    s = Student("cici")
    s.grade = 1
    s.print_info()
    print(s.get_name())
    print(s)
