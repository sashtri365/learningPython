import socket
def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        host = '127.0.0.1'
        port = 8080
        client_socket.connect((host,port))
        print(f"conneted to server")

        massage = " helllo"
        client_socket.send(massage.encode("utf-8"))
        print("masssage send sucessfully. massage:", massage)
        data_income = client_socket.recv(1024)
        print(f"data recived from server: {data_income.upper().decode("utf-8")}")

if __name__== "__main__":
    start_client()