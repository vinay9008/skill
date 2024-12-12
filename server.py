import socket

def server_program():
    host = '127.0.0.1'  # Server's IP address
    port = 7891  # Server's port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Get instance
    server_socket.bind((host, port))  # Bind host address and port together
    server_socket.listen(5)  # Configure how many clients the server can listen to simultaneously

    print("Server is Online")
    conn, address = server_socket.accept()  # Accept new connection
    print("Connection from: " + str(address))

    fname = conn.recv(50).decode()  # Receive the filename
    print("Requesting for file: " + fname)

    try:
        with open(fname, 'r') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                conn.send(data.encode())  # Send file contents to the client
    except FileNotFoundError:
        conn.send("File not found\n".encode())

    print("Request sent")
    conn.close()  # Close the connection

if __name__ == '__main__':
    server_program()
