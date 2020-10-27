# 列表
def list_study():
    arr = list()
    arr2 = []
    print(arr)
    arr2.append("1")
    arr2.append(2)
    # 删除元素
    del arr2[1]
    print(arr2)
    # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    arr2.extend([2, 3])
    print(arr2)


# 元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
def tuple_study():
    t = tuple()
    t2 = (1, 2, 3)
    print(t)
    print(t2)
    print(max(t2))


# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
def set_study():
    s = set()
    s2 = {1, 2, 3, 3}
    print(s)
    # 删除元素
    s2.remove(3)
    # 添加元素
    s2.add(5)
    print(s2)


# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
def dict_study():
    d = dict()
    d2 = {'name': 'wind'}
    print(d)
    d2['age'] = 18
    for k, v in d2.items():
        print(f"key=>{k}, val=>{v}")
    print(d2.keys())
    print(d2.values())
    print(d2)
    del d2['name']  # 删除键 'Name'
    print(d2)
    d2.clear()  # 清空字典
    print(d2)
    del d2  # 删除字典


if __name__ == '__main__':
    list_study()
    tuple_study()
    set_study()
    dict_study()
