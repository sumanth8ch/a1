import socket
from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 5001
clients = {}
addresses = {}
s.bind((HOST,PORT))

def accept_clients() :
    while True :
        c,c_addr = s.accept()
        print("%s:%s has connected." % c_addr)
        c.send("Hello!".encode('utf-8'))
        addresses[c] = c_addr
        Thread(target= handle_client, args=(c,)).start()
def handle_client() :
    name = c.recv(1024).decode('utf-8')
    note = 'To exit, type q'
    c.send(note.encode('utf-8'))
    msg = "%s has joined the chat"% name
    broadcast(msg.encode('utf-8'))
    clients[c] = name
    while True :
        msg = c.recv(1024)

        if msg == 'q':
            c.close()
            del clients[c]
            broadcast("%s has left the chat"% name.encode('utf-8'))
            break
        else :
            broadcast(msg, name+": ")
def broadcast(msg, prefix=" "):
    for i in clients:
        i.send(prefix.encode('utf-8')+msg)
if __name__ == "__main__":
    s.listen(100)
    print("Waiting for connections")
    accept_thread = Thread(target=accept_clients)
    accept_thread.start()
    accept_thread.join()
    s.close()
