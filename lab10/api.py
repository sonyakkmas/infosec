#!/usr/bin/env python3
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        body = json.dumps(data, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/hello":
            self.send_json({"message": "Hello from the API!"})
        elif self.path == "/time":
            self.send_json({"time": datetime.now().isoformat()})
        else:
            self.send_json({
                "path_received": self.path,
                "client_address": self.client_address[0],
                "headers": dict(self.headers),
            })


HTTPServer(("127.0.0.1", 5000), Handler).serve_forever()
