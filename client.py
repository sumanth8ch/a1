import socket,sys,select,string
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST =socket.gethostname()
PORT = 4004
s.settimeout(10)
s.connect((HOST,PORT))
print("Connected to server")
name = input("Enter nickname: ")
s.send(name.encode('utf-8'))
sys.stdout.write("You: ")
sys.stdout.flush()
while 1 :
	sock_list = [s]
	r_list,w_list,e_list = select.select(sock_list,[], [] )
	for i in r_list:
		if i == s:
			msg_rcv = i.recv(4096)
			if not msg_rcv:
				print("DISCONNECTED")
				sys.exit()
			else:
				sys.stdout.write(msg_rcv.decode('utf-8'))
				sys.stdout.write("You: ")
				sys.stdout.flush()
		else:
			msg = sys.stdin.readline()
			s.send(msg.encode('utf-8'))
			sys.stdout.write("You: ")
			sys.stdout.flush()
