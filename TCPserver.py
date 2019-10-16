import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((bind_ip, bind_port))
server.listen(5)

print(f"[*] listening on {bind_ip}, {bind_port}")

def handle_client(client_socket):
    # print what the client sends
    request = client_socket.recv(1024)
    print(f"[*] Received {request}")

    if(request.strip() == ("close connection").encode()):
        print("Exiting console...\n")
        client_socket.send(("Closing connection...\n").encode())
        server.shutdown(socket.SHUT_RDWR)
        server.close()
    client_socket.send(("ACK!").encode())
    client_socket.close()
    

while(True):
    client, addr = server.accept()
    print(f"Accepted connection from {addr[0]} {addr[1]}")
    client_handler = threading.Thread(target=handle_client, args = (client, ))
    client_handler.start()
    
