import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("localhost", 34720)
    sock.bind(addr)

    sock.listen(5)

    while True:
        (connectedSock, clientAddress) = sock.accept()
        print "client connected"
   
    try:
        msg = "Server says: " + sock.recv(1024).decode() 
    except ConnectionAbortedError:
        sock.close()

    sock.sendall(msg.encode())


main()