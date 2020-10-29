import json

if __name__ == '__main__':
    # Python 字典类型转换为 JSON 对象
    data = {
        'no': 1,
        'name': 'wind',
        'url': 'http://www.baidu.com'
    }

    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 字符串对象：", json_str)
    print(type(json_str))

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])
