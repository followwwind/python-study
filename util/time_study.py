import time

if __name__ == '__main__':
    # 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年
    ticks = time.time()
    print("当前时间戳为:", ticks)

    localtime = time.localtime(time.time())
    print("本地时间为 :", localtime)
    print(localtime.tm_year)
    print(localtime.tm_mon)
    # 时间转化为时间戳
    print(time.mktime(localtime))
    # 格式化日期
    date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(date_str)
    # 字符串时间转时间
    print(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))
