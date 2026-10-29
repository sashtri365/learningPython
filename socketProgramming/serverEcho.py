import socket
def start_server():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
      client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #socket lvl maa gara port use garna.
      client_socket.bind(('127.0.0.1',8080))

      client_socket.listen(2)
      print("server is listening at: 127.0.0.1")

      conn,addr = client_socket.accept()
      print(f"connected to {addr} adress")
      try:
         while True:
            data = conn.recv(1024)
            if not data:
               break
            print(f"reveived data from client:{data.decode("utf-8")}")

            conn.sendall(data)
      except NameError:
         print("please enter right input")
      finally:
         print("connection lost.")
if __name__ == "__main__":
   start_server()