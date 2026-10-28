import socket # socket programming use garna lai socket liabrary import gareko.

host = socket.gethostname() #host name tha pauna lai. yaah my computer is host name
print(host)
#host_name = socket.gethostbyname("google.com")
#print(host_name)

port_80 = socket.getservbyport(80,"tcp") #port number tha xa tara name tha xoina vane yo function use garera tha paune
port_443 = socket.getservbyport(443,"tcp") #same 
print(f"yo port 80 ko name: {port_80} ho")
print(port_443)

#creating socket endpoint
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #tcp protocol maa baneko
    print(s)
    print(s.fileno())   

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #udp protocol maa paneko
    print(s.type)
    print(s, s.fileno, s.type)