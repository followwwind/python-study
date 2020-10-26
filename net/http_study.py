import http.client
import urllib
import urllib.parse
import urllib.request
import json
import requests


def http_client():
    conn = http.client.HTTPConnection("httpbin.org")
    data = '{"name":"张三", "age": 12}'.encode('utf-8')  # 或data = json.dumps({"name":"张三", "age": 12})
    headers = {"Content-Type": "application/json"}
    conn.request("POST", '/post', data, headers)
    res = conn.getresponse()
    print(res.read().decode("utf-8"))


def http_urllib():
    data = '{"name":"张三", "age": 12}'.encode('utf-8')
    # 或data = json.dumps({"name":"张三", "age": 12})
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request("http://httpbin.org/post", data=data, headers=headers)
    res = urllib.request.urlopen(req)
    print(res.read().decode("utf-8"))


def http_request():
    data = {"name": "张三", "age": 12}
    headers = {"Content-Type": "application/json"}
    res = requests.post("http://httpbin.org/post", data=json.dumps(data), headers=headers)
    print(res.json())  # 转为字典格式


if __name__ == '__main__':
    http_request()
    # http_client()
    # http_urllib()

