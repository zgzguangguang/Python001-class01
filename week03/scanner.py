import sys
import  threading
from socket import *


def tcp_test(port):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.settimeout(10)
    try:
        sock.connect_ex((target_ip,port))
        lock.acquire()
        print("Opened ports: ",port)
        lock.release()
    except Exception as e:
        print (e)
if __name__ == '__main__':
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)
    lock = threading.Lock()
    for port in range(start_port,end_port):
        t1 = threading.Thread(target=tcp_test,args=(port,))
        t1.start()


