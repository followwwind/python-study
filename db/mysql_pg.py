import datetime
from queue import Queue
from threading import Thread
from time import time

import psycopg2
import pymysql


class ProcessWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue
            page_no, page_num = self.queue.get()
            transfer_data(page_no, page_num)
            self.queue.task_done()


def get_pg_conn():
    return psycopg2.connect(database="test",
                            user="postgres",
                            password="123456",
                            host="127.0.0.1",
                            port="5432")


def get_mysql_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="0follow0",
        database="test",
        charset="utf8")


def get_data(result):
    data_list = list()
    for row in result:
        val_sql = "("
        for i in range(len(row)):
            col = row[i]
            if isinstance(col, datetime.datetime):
                col = col.strftime('%Y-%m-%d %H:%M:%S')
            elif col is None:
                col = "null"
            if isinstance(col, str) and col != "null":
                val_sql += "'%s'" % col
            else:
                val_sql += str(col)
            if i < len(row) - 1:
                val_sql += ","
        val_sql += ")"
        # print(val_sql)
        data_list.append(val_sql)
    return data_list


# 数据传输
def transfer_data(page_no=int, page_num=int):
    mysql_db = get_mysql_conn()
    pg_db = get_pg_conn()
    mysql_cur = mysql_db.cursor()
    pg_cur = pg_db.cursor()
    pg_cur.execute("SELECT * FROM public.user")
    desc = pg_cur.description
    field_list = list()
    for field in desc:
        field_list.append(field[0])
    col_str = ",".join(field_list)
    insert_sql = "insert into public.user(%s) values" % col_str
    query_sql = "select %s from user limit %d,%d" % (col_str, page_no * page_num, page_num)
    mysql_cur.execute(query_sql)
    data = mysql_cur.fetchall()
    data_list = get_data(data)
    # print(data_list)
    insert_sql += ",".join(data_list)
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
    mysql_cur.close()
    pg_db.close()
    mysql_db.close()


if __name__ == '__main__':
    ts = time()
    queue = Queue()
    # Create 10 worker threads
    # 创建四个工作线程
    for x in range(10):
        worker = ProcessWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        # 将daemon设置为True将会使主线程退出，即使worker都阻塞了
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue
    for num in range(100):
        queue.put((num, 1000))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    # 让主线程等待队列完成所有的任务
    queue.join()
    print('time is {}'.format(time() - ts))



