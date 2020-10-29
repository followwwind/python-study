# read
def read():
    f = open('test.txt', 'r')
    for line in f.readlines():
        print(line)
    f.close()
    # 关键词with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
    with open('test.txt', 'r') as f2:
        for line in f2.readlines():
            print(line)


# write
def write():
    f = open('test.txt', 'w+')
    f.writelines("hello world")
    f.close()


if __name__ == '__main__':
    # write()
    read()
