import socket
import time
if __name__== "__main__":
	host="127.0.0.1"
	port=4455
	addr=(host,port)

	client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	data="Connected" 
	data=data.encode("utf-8")
	client.sendto(data,addr)
	while True:
		
		data,addr=client.recvfrom(1024)
		data=data.decode("utf-8")
		print(f"server:{data}")
		received_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		print("Message received at", received_time)
