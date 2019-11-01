import sys
import subprocess
import os
from urllib.parse import urlparse

from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path);
        print("Query: ", parsed.query);
        path = '/home/pi/www' + parsed.path;
        self.send_response(200);
        self.send_header('Content-type', 'text/html');
        self.end_headers();
        self.wfile.write(subprocess.check_output(['python3', path, "none"]));

server = HTTPServer(('', 8000), Handler);
server.serve_forever();

