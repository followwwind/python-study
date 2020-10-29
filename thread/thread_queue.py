import queue
import threading
import time

exitFlag = 0


class MyThread (threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(thread_name, q):
    while not exitFlag:
        print("process_data start, thread_name is %s" % thread_name)
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (thread_name, data))
            q.task_done()
        else:
            queueLock.release()
        time.sleep(1)


queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []


def empty():
    # 等待队列清空
    while not workQueue.empty():
        pass


# queue join跟task_done()配合
def join():
    # 实际上意味着等到队列为空，再执行别的操作
    workQueue.join()


if __name__ == '__main__':
    nameList = ["One", "Two", "Three", "Four", "Five"]
    # 创建新线程
    for i in range(3):
        thread = MyThread(i, "Thread-%d" % i, workQueue)
        thread.start()
        threads.append(thread)
    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()
    empty()
    # join()
    print("queue finish")
    exitFlag = 1
    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")
