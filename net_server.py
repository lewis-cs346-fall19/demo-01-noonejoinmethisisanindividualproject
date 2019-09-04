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
                msg = "Server says: " + connectedSock.recv(1024).decode() 
                connectedSock.sendall(msg.encode())
            except ConnectionAbortedError:
                sock.close()

            

        connectedSock.close()
        break

    sock.close()

main()
