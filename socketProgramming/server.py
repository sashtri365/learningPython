import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 8000
server_socket.bind((HOST,PORT))

server_socket.listen(5)
print(f"server is running on {HOST}:{PORT} and waiting for send/receive data")

conn,address = server_socket.accept() #conn -> create new socket for new user. address -> keep ip+port details
print(f"client is connected : {address}") # address ==>> client address

while True:
    data = conn.recv(1024).decode('utf-8') #conn = new socket, .recv(1024) = recv() data paune function ra 1024 bytes.
    #server le one time maa 1024 (1 kb) data padhna sakxa vanne artha 1024 ko ho. data binary/bytes maa internet maa
    # kudxa so to convert into normal data type we use .decode('utf-8')
    if not data or data.lower() == 'exit':
        print("connection lost")
        break
    print(f"client data: {data}.")

    response = "i got massage."
    conn.send(response.encode('utf-8')) # create response variable and sent

conn.close()
server_socket.close() 