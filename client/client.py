import socket
import sys
import argparse 

parser = argparse.ArgumentParser(
                    prog='client.py',
                    description='What the program does',
                    epilog='-p <port> -h <host>')
parser.add_argument('-p', '--port', type=int, help='Port number to connect to', default=80)
parser.add_argument('-H', '--host', type=str, help='Host name to connect to', default='localhost')
args = parser.parse_args()
print("Using host %s and port %d" % (args.host, args.port))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.host, args.port)
sock.connect(server_address)

while True:
    line = input("Enter a message to send to the server (or 'exit' to quit): ")
    sock.sendall(line.encode('UTF-8'))  # convert to bytes and send
    if line == "exit":
        break
    msg = sock.recv(1024)  
    print(msg.decode('UTF-8'))
    
