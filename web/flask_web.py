import time
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return jsonify({"data": [{"data_cnt": "10", "process_dt": "2020-10-26"}]})


@app.route("/hi", methods=['GET', 'POST'])
def hi():
    request_body = request.get_json()
    pageNo = request_body['pageNo']
    pageSize = request_body['pageSize']
    data_list = list()
    for i in range(int(pageSize)):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data_json = {
            "id": int(pageNo) * int(pageSize) + i,
            "username": "hello%d" % i,
            "password": "123",
            "sex": 0,
            "img": None,
            "email": None,
            "phone": "",
            "create_time": now,
            "update_time": now,
            "del_flag": 0
        }
        data_list.append(data_json)
    return jsonify({"data": data_list})


if __name__ == '__main__':
    app.run()
