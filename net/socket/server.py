import socket


def start():
    # 创建 socket 对象
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    port = 9999
    # 绑定端口号
    server_socket.bind((host, port))
    # 设置最大连接数，超过后排队
    server_socket.listen(5)
    while True:
        # 建立客户端连接
        client_socket, addr = server_socket.accept()
        print("连接地址: %s" % str(addr))
        msg = 'hello world！' + "\r\n"
        client_socket.send(msg.encode('utf-8'))
        client_socket.close()


if __name__ == '__main__':
    start()
