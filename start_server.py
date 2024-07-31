import os
import socket
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

def start_server(port):
    os.chdir(os.path.dirname(__file__))
    httpd = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    print(f"Serving on port {port}...")
    try:
        while True:
            httpd.handle_request()
    except KeyboardInterrupt:
        print("\nServer stopped.")

def open_in_browser(port):
    url = f"http://localhost:{port}"
    print(f"Opening {url} in browser...")
    webbrowser.open(url, new=2)  # new=2 opens in a new tab

def print_instructions(port):
    print(f"Server started. Access your webpage at http://localhost:{port}")
    print("Press Ctrl+C to stop the server.")

if __name__ == "__main__":
    port = find_free_port()
    print_instructions(port)
    open_in_browser(port)
    start_server(port)