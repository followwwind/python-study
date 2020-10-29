import threading
import time


class MyThread (threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self):
        print("开始线程：" + self.name)
        time.sleep(5)
        global count
        count += 1
        print_time(self.name, count)
        print("退出线程：" + self.name)


def print_time(thread_name, num):
    print("name is %s, count is %s" % (thread_name, num))


count = 1

if __name__ == '__main__':
    # 创建新线程
    threads = list()
    for i in range(10):
        t = MyThread(i, "Thread-%d" % i)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print("退出主线程")
