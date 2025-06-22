import json
import os
import socket
import threading
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

# === Константи ===
HOST = 'localhost'
HTTP_PORT = 3000
SOCKET_PORT = 5000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_DIR = os.path.join(BASE_DIR, 'storage')
DATA_FILE = os.path.join(STORAGE_DIR, 'data.json')


# === UDP Socket Server ===
def start_socket_server():
    os.makedirs(STORAGE_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, SOCKET_PORT))
    print(f"[UDP] Socket server running on port {SOCKET_PORT}...")

    while True:
        data, _ = sock.recvfrom(4096)
        try:
            message = json.loads(data.decode('utf-8'))
            timestamp = str(datetime.now())
            with open(DATA_FILE, 'r+') as f:
                all_data = json.load(f)
                all_data[timestamp] = message
                f.seek(0)
                json.dump(all_data, f, indent=2)
        except Exception as e:
            print(f"[UDP] Error: {e}")


# === HTTP Server ===
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': 'index.html',
            '/message.html': 'message.html',
            '/error.html': 'error.html',
            '/style.css': 'style.css',
            '/logo.png': 'logo.png'
        }

        file_path = routes.get(self.path, 'error.html')
        content_type = 'text/html'

        if file_path.endswith('.css'):
            content_type = 'text/css'
        elif file_path.endswith('.png'):
            content_type = 'image/png'

        try:
            with open(os.path.join(BASE_DIR, file_path), 'rb') as f:
                self.send_response(200 if self.path in routes else 404)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(body)

            username = data.get('username', [''])[0]
            message = data.get('message', [''])[0]

            payload = json.dumps({
                'username': username,
                'message': message
            })

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(payload.encode('utf-8'), (HOST, SOCKET_PORT))

            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')


# === Запуск ===
def start_http_server():
    server = HTTPServer((HOST, HTTP_PORT), SimpleHTTPRequestHandler)
    print(f"[HTTP] Server running on http://{HOST}:{HTTP_PORT}")
    server.serve_forever()


if __name__ == '__main__':
    t1 = threading.Thread(target=start_http_server)
    t2 = threading.Thread(target=start_socket_server)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
