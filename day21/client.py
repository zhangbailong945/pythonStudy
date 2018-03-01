import sys
import socket

#创建一个socket对象
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名词
host=socket.gethostname()
port=9999

#连接服务，指定主机和端口
clientsocket.connect((host,port))
#接受小于1024字节的数据
msg=clientsocket.recv(1024)
clientsocket.close()
print(msg.decode('utf-8'))