import socket,sys
from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv) < 2):
    print("ENTER: python chatserver.py hostname:port")
    sys.exit()
in_list = sys.argv[1].split(':')
HOST =in_list[0]
PORT = int(in_list[1])
clients = {}
cli_sockets = []
s.bind((HOST,PORT))

def accept_clients() :
    while True :
        c,c_addr = s.accept()
        print("%s:%s has connected." % c_addr)
        c.send("Hello 1".encode('utf-8'))
        cli_sockets.append(c)
        Thread(target= handle_client, args=(c,c_addr)).start()

def handle_client(c,c_addr) :

    name = c.recv(1024).decode('utf-8')
    msg = "%s has joined the chat \n"% name
    broadcast(msg,c)
    clients[c] = name
    while True :
        msg = c.recv(1024).decode('utf-8')
        if not msg:
            c.close()
            del clients[c]import socket,sys, re
            from threading import Thread
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if (len(sys.argv) < 2):
                print("ENTER: python chatserver.py hostname:port")
                sys.exit()
            in_list = sys.argv[1].split(':')
            HOST =in_list[0]
            PORT = int(in_list[1])
            clients = {}
            cli_sockets = []
            s.bind((HOST,PORT))

            def accept_clients() :
                while True :
                    c,c_addr = s.accept()
                    print("%s:%s has connected." % c_addr)
                    c.send("Hello 1 \n")
                    cli_sockets.append(c)
                    Thread(target= handle_client, args=(c,c_addr)).start()

            def handle_client(c,c_addr) :

                n = c.recv(1024)
                name = n.strip("NICK ")
                if len(name)<=12 and re.match("^[A-Za-z0-9\_]+$",name) is not None:
                    c.send("OK \n")
                else :
                    c.send(" ERROR - nickname is not valid \n")
                    name = 'unkwown'
                msg = "%s has joined the chat \n"% name
                broadcast(msg,c)
                clients[c] = name
                while True :
                    m = c.recv(1024).decode('utf-8')
                    msg = m.strip("MSG ")
                    if not msg:
                        c.close()
                        del clients[c]
                        snd = "%s has left the chat \n"% name
                        print("%s:%s has diconnected." % c_addr)
                        broadcast(snd,c)
                        break
                    else :
                        if len(msg) > 255 and re.match("^[^\x00-\x7F]*$",msg) is None:
                            c.send("ERROR - message is not valid")
                            msg_snd = "MSG "+name +" "
                        else:
                            msg_snd = "MSG "+name +" "+ msg
                        broadcast(msg_snd,c)

            def broadcast(msg, cli_conn):
                for i in cli_sockets:
                    if i != s and i != cli_conn :
                        try:
                            i.send(msg.encode('utf-8'))
                        except:
                            pass

            while True:
                s.listen(100)
                print("Waiting for connections")
                accept_thread = Thread(target=accept_clients)
                accept_thread.start()
                accept_thread.join()
                s.close()

            snd = "%s has left the chat \n"% name
            broadcast(snd,c)
            break
        else :
            msg_snd = name + ": " + msg
            broadcast(msg_snd,c)

def broadcast(msg, cli_conn):
    for i in cli_sockets:
        if i != s and i != cli_conn :
            try:
                i.send(msg.encode('utf-8'))
            except:
                pass

while True:
    s.listen(100)
    print("Waiting for connections")
    accept_thread = Thread(target=accept_clients)
    accept_thread.start()
    accept_thread.join()
    s.close()
