from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandller(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/template/index.html'
        elif self.path == '/second':
            self.path = '/template/second.html'

        try:
            fileOpen = open(self.path[1:]).read()
            self.send_response(200)

        except:
            fileOpen = "File Not Found :3 "
            self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(fileOpen.encode())

if __name__ == '__main__':
    port = 8000
    servername = 'localhost'
    server = HTTPServer((servername, port), helloHandller)
    print("Server started http://%s:%s" % (servername, port))
    server.serve_forever()
