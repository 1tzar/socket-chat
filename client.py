import socket
import threading
import sys
import pickle
class Client:
    #Сhange this port other way this won't work
    def __init__(self,host = "localhost", port = 4000):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((str(host),int(port)))
        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.deamon = True
        msg_recv.start()

        while True:
            msg = input("->")
            if msg != "-out":
                self.send_msg(msg)
            else:
                self.socket.close()
                sys.exit()

    def msg_recv(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    def send_msg(self,msg):
        self.socket.send(pickle.dumps(msg))


c = Client()