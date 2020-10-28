# read
def read():
    f = open('test.txt', 'r')
    for line in f.readlines():
        print(line)
    f.close()


# write
def write():
    f = open('test.txt', 'w+')
    f.writelines("hello world")
    f.close()


if __name__ == '__main__':
    write()
    read()
