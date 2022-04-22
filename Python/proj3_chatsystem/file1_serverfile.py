import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # to make object of socket

server_socket.bind(('127.0.0.1', 5080))

server_socket.listen(10)   # max how much connection to accept at one time
print("[+] Listening for connection on 127.0.0.1:5090.. ")

while True:  # use while true if you are not sure how much loop will be used or used for infinity loops
    conn, addr = server_socket.accept()
    # conn = store connection or request from Clients ,   addr = store address of client
    print(" [+] got a connection from {}".format(addr))
    
    while True:

        data = conn.recv(2024)  # to receive data send by user  1024 means it can receive 1024 bytes at a time
        if(data.decode() == 'bye'): break
        print("[+] client sent: ", data.decode())

        # to send data by developer
        server_data = input(" Enter data to send: ")
        conn.send(server_data.encode())
        conn.send(b'this is server ')  # b means it sends in byte format

    conn.close()
    print("[+] Click to disconnect... ")
