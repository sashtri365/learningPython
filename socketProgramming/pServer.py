import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
    ss.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    
    host = "127.0.0.1"
    port = 9001
    
    ss.bind((host,port))
    ss.listen(5)
    print(f"server is listening at: {host}")
    
    conn,addr = ss.accept()
    print(f"user connected from {addr} adress")
    
    while True:
     try:
        massage = input("enter your massage: ")
        conn.send(massage.encode('utf-8'))

        data_recv = conn.recv(1024)
        print(f"data received from client. Data:{data_recv.decode("utf-8")}")
    
        if not data_recv or data_recv.decode().strip().lower() == 'exit':
            print(f"this {addr} client cut  connection")
            break
     except ConnectionResetError:
        print("user cut the connection")
        break   

    #  ss.close()  is optional if yo use with(context manager)