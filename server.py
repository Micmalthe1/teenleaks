# server.py

import http.server
import socketserver
import random

# Read lines from the document
with open('keys.txt', 'r') as file:
    lines = file.readlines()

# Define a handler to serve the random line
class RandomLineHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Choose a random line
        random_line = random.choice(lines)

        # Remove the chosen line from the list (optional)
        lines.remove(random_line)

        # Save the updated content back to the file (optional)
        with open('keys.txt', 'w') as updated_file:
            updated_file.writelines(lines)

        self.wfile.write(random_line.encode())

# Start the server
port = 8000
httpd = socketserver.TCPServer(('', port), RandomLineHandler)
print(f'Serving on port {port}...')
httpd.serve_forever()
