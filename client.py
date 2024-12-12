import socket

def client_program():
    host = '127.0.0.1'  # Server's IP address
    port = 7891  # Server's port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Instantiate
    client_socket.connect((host, port))  # Connect to the server

    print("Client is connected to Server")
    fname = input("Enter file name: ")  # Take input

    client_socket.send(fname.encode())  # Send the filename to the server
    print("\nReceived response\n")

    while True:
        data = client_socket.recv(1024).decode()  # Receive response
        if not data:
            break
        print(data)  # Print the received data

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()
