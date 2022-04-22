import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5080))  # to connect with server
print("[+] Trying to connect to 127.0.0.1: 5080")

while True:

    data = input(" Enter data to send: ")
    client_socket.send(data.encode())  # to send data to server
    server_data = client_socket.recv(2024)   # to receive data

    if(server_data == ''): break
    if (data == 'bye'): break

    print('[+] server sent: ', server_data.decode())

