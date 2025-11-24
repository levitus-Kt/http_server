import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/main':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1Main page</h1>')
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>About</h1>')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"<h1>404: Not found</h1>")

        # return super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Сервер запущен на", PORT)
    httpd.serve_forever()