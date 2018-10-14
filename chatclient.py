import socket,sys,select,string
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv) < 3):
	print("ENTER: python chatclient.py hostname port")
	sys.exit()
HOST =sys.argv[1]
PORT = int(sys.argv[2])
s.settimeout(10)
s.connect((HOST,PORT))
print("Connected to server")
name = raw_input("Enter nickname: ")
s.send(name.encode('utf-8'))


while 1 :
	sock_list = [sys.stdin,s]
	r_list,w_list,e_list = select.select(sock_list,[], [] )
	for i in r_list:
		if i == s:
			msg_rcv = i.recv(1024)
			if not msg_rcv:
				print("DISCONNECTED")
				sys.exit()
			else:
			    	sys.stdout.write(msg_rcv)
				sys.stdout.write("You: ")
				sys.stdout.flush()
		else:
        		msg = sys.stdin.readline()
			s.send(msg.encode('utf-8'))
			sys.stdout.flush()

s.close()


				
