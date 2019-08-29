import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("9.293.82.19", 34720)
    sock.bind(addr)

    sock.listen(8)

    while True:
        (connectedSock, clientAddress) = sock.accept()
   
    try:
        msg = sock.recv(1024).decode() 
    except ConnectionAbortedError:
        sock.close()

    sock.sendall(msg.encode())


main()