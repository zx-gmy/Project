"""
http server
io多路复用，类封装练习
"""
from socket import *
from select import *
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dor=None):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.dir = dir
        # 多路复用监控列表
        self.rlist = []
        self.wlist = []
        self.xlist = []

        self.sockfd = socket()
        self.sockfd.setblocking(False)
        self.sockfd.bind(self.address)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
