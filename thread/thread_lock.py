import threading
import time

count = 0
threadLock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self):
        # safe_count()
        unsafe_count()


def safe_count():
    global count
    for i in range(100000):
        threadLock.acquire()
        count += 1
        threadLock.release()


def unsafe_count():
    global count
    for i in range(100000):
        count += 1


if __name__ == '__main__':
    # 创建新线程
    threads = list()
    for i in range(3):
        t = MyThread(i, "Thread-%d" % i)
        t.start()
        threads.append(t)
    # 返回一个包含正在运行的线程的list
    while len(threading.enumerate()) != 1:
        time.sleep(1)
    # for t in threads:
    #     t.join()
    print(count)
    print("退出主线程")
