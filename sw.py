#!/usr/bin/python3
import socket, sys, os, time

def help():

	print(r"""Usage: python3 sw.py -l 4444           [SERVER LISTENER]
       python3 sw.py 127.0.0.1 4444    [CONNECT TO (with netcat by the moment)]""")


def netcat_connect():

	os.system('nc ' + sys.argv[1] + " " + sys.argv[2])

def listen(ip,port):
	buffer=9999999
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((ip, port))
	s.listen(1)
	print("listening on port " + str(port) + " ...")
	conn, addr = s.accept()
	print('connect to',addr[0],'from',addr[0],addr[1])
	while True:

		ans = conn.recv(buffer).decode()
		sys.stdout.write(ans)
		command = input()

		command += "\n"
		conn.send(command.encode())
		time.sleep(0.1)     #this made the trick

		########################################################
		# TUNE ME IF YOU ARE TRYING TO CONNECT TO A BASH SHELL #
		########################################################
		# by removing the output of the "input()" function     #
#		sys.stdout.write("\033[A" + ans.split("\n")[-1])       #
		########################################################

if (len(sys.argv) < 3):
	help()
	sys.exit(1)

if sys.argv[1] == "-l":
	port = int(sys.argv[2])
	listen("0.0.0.0",port)
else:

	netcat_connect()

