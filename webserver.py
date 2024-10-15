import os
import socket
import subprocess


HOST, PORT = 'localhost', 8080

PROJECT_ROOT = '/Applications/project_root'  


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
    elif file_path.endswith(".gif"):
        return "image/gif"
    elif file_path.endswith(".svg"):
        return "image/svg+xml"
    elif file_path.endswith(".ico"):
        return "image/x-icon"
    return "text/plain"

def find_file(requested_file):
    file_path = os.path.join(PROJECT_ROOT, requested_file.lstrip('/'))
    print(f"Tìm kiếm file: {file_path}")  
    return file_path if os.path.exists(file_path) else None

def handle_php(file_path):
    try:
        result = subprocess.run(["php-cgi", file_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout  
        else:
            return f"PHP Error: {result.stderr}"  
    except Exception as e:
        return f"Error: {str(e)}"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Serving on port {PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected by {client_address}")
            request = client_socket.recv(1024).decode()
            print(f"Request: {request}")

           
            request_line = request.splitlines()[0]
            requested_file = request_line.split(" ")[1]
            

            
            
            if requested_file == '/':
                requested_file = '/index.html'  
            else:
    
                full_path = os.path.join(PROJECT_ROOT, requested_file.lstrip('/'))
                if os.path.isdir(full_path): 
                    requested_file = os.path.join(requested_file, 'index.html')

            
            file_path = find_file(requested_file)

           
            if file_path:
                mime_type = get_mime_type(file_path)

               
                with open(file_path, 'rb') as file:
                    file_content = file.read()

                response = f'HTTP/1.1 200 OK\nContent-Type: {mime_type}\n\n'.encode() + file_content
            else:
                
                print(f"File không tồn tại: {requested_file}")  
                response = 'HTTP/1.1 404 NOT FOUND\n\nPage Not Found'.encode()

            client_socket.sendall(response) 