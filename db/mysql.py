import time

import pymysql


def get_conn():
    # 打开数据库连接
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="0follow0",
        database="test",
        charset="utf8")


def select_version():
    conn = get_conn()
    # 获取连接下的游标
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询，查询数据库版本
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法返回一条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # 关闭数据库连接
    conn.close()


def insert_sql():
    time_start = time.time()
    conn = get_conn()
    # 获取连接下的游标
    cursor = conn.cursor()
    sql = """insert into user (id, username, password, sex, create_time, update_time, del_flag) 
    values (%d, %s, %s, %d, %s, %s, %d)"""
    for i in range(0, 1000000):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        tmp_sql = sql % (i, str(i), str(i), 0, "'%s'" % now, "'%s'" % now, 0)
        try:
            # 执行sql语句
            cursor.execute(tmp_sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
            # 关闭数据库连接
    conn.close()
    time_end = time.time()
    print('totally cost', time_end - time_start)


def select_many():
    conn = get_conn()
    # 获取连接下的游标
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询，查询数据库版本
    cursor.execute("SELECT * FROM user LIMIT 10")
    data = cursor.fetchall()
    for row in data:
        print(row)
    # 关闭数据库连接
    conn.close()


def show_col():
    conn = get_conn()
    # 获取连接下的游标
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询，查询数据库版本
    cursor.execute("SELECT * FROM user")
    desc = cursor.description
    for field in desc:
        print(field[0])
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # select_version()
    # insert_sql()
    select_many()
    show_col()
