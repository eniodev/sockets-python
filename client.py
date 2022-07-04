import socket



PORT = 5050


HEADER = 64
FORMAT = 'utf-8'

SERVER  = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
DISC_MESSAGE = "LEFT THE ROOM"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_len = str(msg_length).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

send('Hello') 

send(DISC_MESSAGE)