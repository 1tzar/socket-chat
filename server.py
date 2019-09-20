import socket
import threading
import sys
import pickle
class Server:
    def __init__(self,host = "localhost", port = 4000):
        name = ''
        self.clients = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((str(host),int(port)))
        self.socket.listen(10)
        self.socket.setblocking(False)

        accept = threading.Thread(target = self.acceptCon)
        process = threading.Thread(target = self.processCon)

        accept.daemon = True
        accept.start()

        process.daemon = True
        process.start()

        while True:
            msg = input('->')
            if msg == '-out':
                self.socket.close()
                sys.exit()
            else:
                pass



    def acceptCon(self):
        print('Server running...')
        while True:
            try:
                conn,adr = self.socket.accept()
                conn.setblocking(False)
                self.clients.append(conn)
            except Exception as a:
                pass

    def broadcast(self,msg, client ):
        for i in self.clients:
            try:
                if  i != client:
                    i.send(msg)
            except:
                self.clients.remove(i)

    def processCon(self):
        print('Server running...')
        while True:
            if len(self.clients) > 0:
                for c in self.clients:
                    try:
                        data = c.recv(1024)

                        if data:
                            self.broadcast(data,c)
                    except:
                        pass
s = Server()
