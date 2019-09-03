import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("localhost", 34720)
    sock.connect(addr)
    
    for i in range(100):
        msg = str(i)
        sock.sendall(msg.encode())
        msg = sock.recv(1024).decode()
        print(msg)
    
    sock.close()

main()
