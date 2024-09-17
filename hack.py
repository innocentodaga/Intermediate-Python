import socket
practice = socket.socket()
practice.connect(("192.168.1.107", 22))
sample = practice.recv(1024)
print (sample)
practice.close
