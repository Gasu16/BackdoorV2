import socket
from sys import argv

script, message = argv
#target_host = "www.google.com"
target_port = 9999
target_host = "0.0.0.0"



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(message.encode())
#client.send(("\nGET / HTTP/1.1\r\nHost: google.com\r\n\r\n").encode())

response = client.recv(4096)

print(f"RESPONSE: \n\n{response}")
