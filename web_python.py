import sys
import subprocess
import os
from urllib.parse import urlparse
import json

DEFAULT_CONFIG = {
    "base_directory": "/var/www/html",
    "port": 8000,
    "bind_ip": "localhost",
}

if(not os.path.exists('config.json')):
    with open('config.json', 'w') as file:
        file.write(json.dumps(DEFAULT_CONFIG, indent=4));
        file.flush();

CONFIG = dict();
with open('config.json') as file:
    CONFIG = json.loads(file.read());

from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path);
        print("Query: ", parsed.query);
        path = CONFIG['base_directory'] + parsed.path;
        self.send_response(200);
        self.send_header('Content-type', 'text/html');
        self.end_headers();
        self.wfile.write(subprocess.check_output(['python3', path, parsed.query]));

server = HTTPServer((CONFIG['bind_ip'], int(CONFIG['port'])), Handler);
server.serve_forever();

