import socket,sys,select,string
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv) < 3):
    print("ENTER: python chatclient.py hostname:port nickname")
    sys.exit()
in_list = sys.argv[1].split(':')
HOST =in_list[0]
PORT = int(in_list[1])
nickname = sys.argv[2]
s.settimeout(10)
s.connect((HOST,PORT))
print("Connected to server")
nick = 'NICK '+ nickname
s.send(nick)
a =''

while 1 :
    sock_list = [sys.stdin,s]
    r_list,w_list,e_list = select.select(sock_list,[], [])
    for i in r_list:
        if i == s:
            msg_rcv = i.recv(1024)
            if not msg_rcv:
                print("DISCONNECTED")
                sys.exit()
            else:
                    if msg_rcv != 'MSG '+nickname+' '+a :
                        sys.stdout.write(msg_rcv.strip('MSG '))
                        sys.stdout.flush()
                    else :
                        continue


        else:
                a = ''
                msg = sys.stdin.readline()
                a += msg
                ms ='MSG ' + msg
                s.send(ms.encode('utf-8'))
                sys.stdout.write("You : ")
                sys.stdout.write(msg)
                sys.stdout.flush()

s.close()
