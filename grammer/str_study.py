import datetime


def base():
    s = "hello world"
    print(s[0])
    print(s[0:5])
    print("my name is %s, age is %d" % ("wind", 18))
    # find跟index一样，如果子字符串不存在会报异常
    print(s.find("hello"))
    print(f'{s[0: 5]}')
    d = datetime.datetime.now()
    s = f"{d:%Y-%m-%d %A %p %H:%M:%S.%f}"
    print(s)


def func():
    print(str(3.14))
    # Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
    print(b"3".isdigit())
    # Unicode数字，全角数字（双字节），罗马数字，汉字数字
    print("三".isnumeric())
    # Unicode数字，，全角数字（双字节)
    print("3".isdecimal())
    # 替换字符串，-1表示所有，1表示一次
    print("hello world world".replace("world", "kitty", -1))
    seq = ("hello", "kitty")  # 字符串序列
    print(",".join(seq))
    print(len("hello"))
    print("   ".isspace())


if __name__ == '__main__':
    base()
    func()
