import os
import socket

HOST, PORT = 'localhost', 8080

def get_mime_type(file_path):
    if file_path.endswith(".html"):
        return "text/html"
    elif file_path.endswith(".css"):
        return "text/css"
    elif file_path.endswith(".js"):
        return "application/javascript"
    elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
        return "image/jpeg"
    elif file_path.endswith(".png"):
        return "image/png"
    return "text/plain"

def handle_request(request):
    request_line = request.splitlines()[0]
    requested_file = request_line.split(" ")[1]

    if requested_file == '/':
        requested_file = '/index.html'

    file_path = 'WEB_ROOT' + requested_file

    if os.path.exists(file_path):
        mime_type = get_mime_type(file_path)
        with open(file_path, 'rb') as file:
            file_content = file.read()

        response = f'HTTP/1.1 200 OK\nContent-Type: {mime_type}\n\n'.encode() + file_content
    else:
        response = 'HTTP/1.1 404 NOT FOUND\n\nPage Not Found'.encode()

    return response

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Serving on port {PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                request = client_socket.recv(1024).decode()
                if request:
                    print(f"Request: {request}")
                    response = handle_request(request)
                    client_socket.sendall(response)

if __name__ == "__main__":
    start_server()
