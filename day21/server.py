import sys
import socket

#创建一个socket对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host=socket.gethostname()
#端口
port=9999
#绑定主机和端口
serversocket.bind((host,port))
#设置最大连接输，超过后排队
serversocket.listen(5)

#建立阻塞队列
while True:
    #建立客户端连接
    clientsocket,addr=serversocket.accept()
    print("连接地址：%s"%str(addr))
    msg='欢迎访问菜鸟教程！'+"\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
