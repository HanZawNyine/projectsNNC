# echo_server.py
import socket
import threading


def main(host, port):
    # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    while True:
        print(f'[*] Listening on {host}:{port}')
        conn, addr = s.accept()
        #print('aaaa', addr)
        print(f'connected by {addr[0]} : {addr[1]}')

        client_handler = threading.Thread(target=handle_client, args=(conn,))
        client_handler.start()
        # conn.close()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024).decode('utf-8')
        print(f'[*] Received: {request}')
        request = request.split(' ')
        request_page = request[1]
        print("request", request[1])
        if request_page == '/':
            data = '/template/index.html'
            print("------------------------", data)

        try:
            fileOpen = open(data[1:]).read()
            print("open : ", fileOpen)
           # socket.send_response(200)

        except:
            fileOpen = "File Not Found :3 "
        print(fileOpen)
    # sock.send_response(404)
    #sock.send_header("Content-type", "text/html")
    # sock.end_headers()
    # sock.wfile.write(fileOpen.encode())

    # sock.send(bytes(data))
    # sock.send(b'122')
        # sock.send(fileOpen)


host = 'localhost'        # Symbolic name meaning all available interfaces
port = 8000
main(host, port)
