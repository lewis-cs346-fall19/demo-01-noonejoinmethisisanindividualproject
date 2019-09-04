import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("localhost", 34720)
    sock.bind(addr)

    sock.listen(5)

    while True:
        (connectedSock, clientAddress) = sock.accept()
        print("client connected")
        
        while True:
            try:
                msg = connectedSock.recv(1024).decode()
                if len(msg) == 0: break
                msg = "Server says: " + msg
                connectedSock.sendall(msg.encode())
            except ConnectionAbortedError:
                sock.close()

        
        connectedSock.close()
        break

    sock.close()


main()
