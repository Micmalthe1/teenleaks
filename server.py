import http.server
import socketserver
import random

with open('keys.txt', 'r') as file:
    lines = file.readlines()

class RandomLineHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        random_line = random.choice(lines)


        lines.remove(random_line)


        with open('keys.txt', 'w') as updated_file:
            updated_file.writelines(lines)

        self.wfile.write(random_line.encode())

port = 5000
httpd = socketserver.TCPServer(('', port), RandomLineHandler)
print(f'Serving on port {port}...')
httpd.serve_forever()
