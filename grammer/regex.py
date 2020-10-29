import re

# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
# 而 re.search 匹配整个字符串，直到找到一个匹配。
if __name__ == '__main__':
    line = "Cats are smarter than dogs"
    searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        print("searchObj.group(2) : ", searchObj.group(2))
    else:
        print("Nothing found!!")

    t = re.match('hello', 'hello world').span()
    print(type(t))
    print(t)  # 在起始位置匹配
    print(re.match('world', 'hello world'))  # 不在起始位置匹配
    pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
    print(pattern.match("123sd"))
