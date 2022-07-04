


import socket

import threading



PORT = 5050


HEADER = 64
FORMAT = 'utf-8'
SERVER  = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISC_MESSAGE = "LEFT THE ROOM"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(con, addr):
    print(f"[NEW USER] {addr}")

    connected = True
    while connected:
        msg_length = con.recv(HEADER).decode(FORMAT)
        if msg_length:
           

            msg_length = int(msg_length)
            msg = con.recv(HEADER).decode(FORMAT)
            if msg == DISC_MESSAGE:
                connected = False
                print(f"[{addr}] {DISC_MESSAGE}")
            print(f"[{addr}] {msg}")
    con.close()



def start():
    server.listen()
    while True:
        con, addr = server.accept()
        thread =  threading.Thread(target=handle_client, args=(con, addr))
        thread.start()
        print(f"[ACTIVE USERS, {threading.activeCount()-1}")
print("Server Starting...")
start()


