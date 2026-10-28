import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',8000)) #connect to server

client_socket.send("hello".encode('utf-8'))
response = client_socket.recv(1024).decode('utf-8')
print(f"get response from server: {response}")

client_socket.close()