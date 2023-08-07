#!/usr/bin/python3
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from termcolor import colored

ASCII_ART = """
   __ _________________    __   _     __                  
  / // /_  __/_  __/ _ \  / /  (_)__ / /____ ___  ___ ____
 / _  / / /   / / / ___/ / /__/ (_-</ __/ -_) _ \/ -_) __/
/_//_/ /_/   /_/ /_/    /____/_/___/\__/\__/_//_/\__/_/   
                                                          
"""

USAGE = """
- Usage: python3 HTTPListener.py [HOST] [PORT]
"""

HOST = "localhost"
PORT = 8000

class HTTPListener(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(colored(post_data.decode('utf-8'), "cyan"))
        

if __name__ == "__main__":
    print(colored(ASCII_ART, "green"))
    print(colored(USAGE, "red"))

    if len(sys.argv) > 1:
        HOST = sys.argv[1]
    elif len(sys.argv) > 2:
        PORT = int(sys.argv[2])
    else:
        pass

    server = HTTPServer((HOST, PORT), HTTPListener)
    print(f"Server started on http://{HOST}:{PORT}")

    try:
        print(colored("Server is listening...\n", "yellow"))
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    print("Server stopped")
