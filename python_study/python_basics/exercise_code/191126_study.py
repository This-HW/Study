import socket


class Socketserver:
    def __init__(self, address='', port = 9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.cdata = ''

    def waitforconnection(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connected to', self.addr)
        return 1

    def recvmsg(self):
        self.cdata = ''
        while True:
            data = self.conn.recv(10000)
            self.cdata += data.decode("utf-8")
            if not data:
                break

            self.conn.send(bytes(self.cdata, "utf-8"))  # loop back test

            return self.cdata

        def __del__(self):
            print('sock close')
            self.sock.close()


##########################################

serv = Socketserver('192.168.11.65', 9090)
serv.waitforconnection()

while True:
    msg = serv.recvmsg()
    print('received data : ', msg);
