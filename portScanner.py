from socket import *
from multiprocessing import *

def worker(ip,port):

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.settimeout(1)

    try:
        clientSocket.connect((ip,port))
        clientSocket.close()
        print("port", port, "open" )
    except:
        return
    return

def portScanner(ip,portMax):
    #print statements to seperate ports found on different IP-addresses
    print("_______________________")
    print(ip)
    #Made maximum of 10 processes running at a single time can be changed to increase or decrease speed
    maxProcesses = 10
    for i in range(0,portMax+1):
        proc = Process(target=worker,args=(ip, i))
        proc.start()
        while(len(active_children()) > maxProcesses):
            continue
    #Wait till all processes finish
    while(len(active_children()) > 0):
            continue
    return

