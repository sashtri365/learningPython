import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
    cs.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    
    cs.connect(('127.0.0.1',9001))
    print("connected to host: 127.0.0.1 sucessfully")
 
    while True:
        data_form_server = cs.recv(1024).decode("utf-8")
        print(f"recived data: {data_form_server}")

        if not data_form_server or data_form_server.strip().lower() == 'exit':
            print("connection lost..")
            break

        reply = input("send massage to server: ")
        cs.sendall(reply.encode('utf-8'))