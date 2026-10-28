import socket
import sys

import numpy as np
import pyfiglet as pf

HOST = ""
PORT = 7000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST, PORT))
except socket.error:
    print("Bind failed.", flush=True)
    sys.exit(1)
print("Begin Listening", flush=True)
sock.listen(2)

conn, addr = sock.accept()
print(
    "Established connection with " + addr[0] + ":" + str(addr[1]),
    flush=True,
)

while True:
    data = conn.recv(1024)
    if not data:
        break

    line = data.decode("UTF-8").strip()
    if line == "exit":
        break

    try:
        values = [float(value.strip()) for value in line.split(", ")]
        temp = np.log(np.array(values))
        print(pf.figlet_format(str(temp), font="big"), flush=True)
        conn.sendall(("Received: " + str(temp)).encode("UTF-8"))
    except ValueError:
        print("Invalid input: " + line, flush=True)
        conn.sendall(("Invalid input: " + line).encode("UTF-8"))

conn.close()
sock.close()
