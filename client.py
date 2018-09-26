import socket,sys,select
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST ='18.219.51.6'
PORT = 4711
s.settimeout(1)
s.connect(('18.219.51.6',4711))
print("Connected to server")
name = raw_input("Enter nickname: ")
s.send(name)
sys.stdout.write("You: ")
sys.stdout.flush()
while 1 :
	sock_list = [sys.stdin,s]
	r_list,w_list,e_list = select.select(sock_list,[], [] )
	for i in r_list:
		if i == s:
			msg_rcv = i.recv(4096)
			if not msg_rcv:
				print("DISCONNECTED")
				sys.exit()
			else:
				sys.stdout.write(msg_rcv)
				sys.stdout.write("You: ")
				sys.stdout.flush()
		else:
			msg = sys.stdin.readline()
			s.send(msg)
			sys.stdout.write("You: ")
			sys.stdout.flush()

