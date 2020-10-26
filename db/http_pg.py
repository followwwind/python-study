import json
from queue import Queue
from threading import Thread, Lock
import time
import psycopg2
import requests


class ProcessWorker(Thread):
    def __init__(self, queue, field_list):
        Thread.__init__(self)
        self.queue = queue
        self.field_list = field_list

    def run(self):
        while True:
            # Get the work from the queue
            page_no, page_num = self.queue.get()
            transfer_data(page_no, page_num, self.field_list)
            self.queue.task_done()


def get_pg_conn():
    return psycopg2.connect(database="test",
                            user="postgres",
                            password="123456",
                            host="127.0.0.1",
                            port="5432")


def get_http_sign():
    data = {}
    headers = {"content-type": "application/json", "API-TOKEN": ""}
    url = "http://127.0.0.1:5000/hello"
    res = requests.post(url, data=json.dumps(data), headers=headers)
    result = res.json()
    return result['data'][0]


def get_http_data(pageNo, pageSize):
    data = {"pageNo": pageNo, "pageSize": pageSize}
    headers = {"content-type": "application/json", "API-TOKEN": ""}
    url = "http://127.0.0.1:5000/hi"
    res = requests.post(url, data=json.dumps(data), headers=headers)
    result = res.json()
    return result['data']


def get_col_list():
    pg_db = get_pg_conn()
    pg_cur = pg_db.cursor()
    pg_cur.execute("truncate table public.user")
    pg_cur.execute("SELECT * FROM public.user")
    desc = pg_cur.description
    field_list = list()
    for field in desc:
        field_list.append(field[0])
    pg_cur.close()
    pg_db.close()
    return field_list


# 数据传输
def transfer_data(page_no=int, page_num=int, field_list=list):
    pg_db = get_pg_conn()
    pg_cur = pg_db.cursor()
    data_list = get_http_data(page_no, page_num)
    col_str = ",".join(field_list)
    insert_sql = "insert into public.user(%s) values" % col_str
    val_list = list()
    for row in data_list:
        val_sql = "("
        for i in range(len(field_list)):
            col = row[field_list[i]]
            if col is None:
                col = "null"
            if isinstance(col, str) and col != "null":
                val_sql += "'%s'" % col
            else:
                val_sql += str(col)
            if i < len(row) - 1:
                val_sql += ","
        val_sql += ")"
        val_list.append(val_sql)
    # print(data_list)
    insert_sql += ",".join(val_list)
    # print(insert_sql)
    try:
        # 执行sql语句
        pg_cur.execute(insert_sql)
        # 提交到数据库执行
        pg_db.commit()
    except:
        # 如果发生错误则回滚
        pg_db.rollback()
        # 关闭数据库连接
    pg_cur.close()
    pg_db.close()


def start_job(total, pageSize):
    ts = time.time()
    queue = Queue()
    # Create 10 worker threads
    field_list = get_col_list()
    for x in range(10):
        worker = ProcessWorker(queue, field_list)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        # 将daemon设置为True将会使主线程退出，即使worker都阻塞了
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue
    for num in range(total):
        queue.put((num, pageSize))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    # 让主线程等待队列完成所有的任务
    queue.join()
    print('time is {}'.format(time.time() - ts))


def time_job():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("current sys time is %s" % now)
    sign_result = get_http_sign()
    data_cnt = sign_result['data_cnt']
    process_dt = sign_result['process_dt']
    global sys_dt
    print("sys_dt is %s" % sys_dt)
    if sys_dt == process_dt:
        return
    lock.acquire()
    print("start job")
    sys_dt = time.strftime("%Y-%m-%d", time.localtime())
    # print(sys_dt)
    start_job(int(data_cnt), 1000)
    time.sleep(10)
    lock.release()


def print_time():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("current sys time is %s" % now)


sys_dt = None
lock = Lock()


def main():
    while True:
        time_job()
        time.sleep(10)


if __name__ == '__main__':
    main()

