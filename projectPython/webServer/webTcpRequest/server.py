"""
 Implements a simple HTTP/1.0 Server

"""

import socket


# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print("Server started http://%s:%s" % (SERVER_HOST, SERVER_PORT))

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Get the content of htdocs/index.html
    fin = open('template/index.html')
    content = fin.read()
    fin.close()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n'+content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()