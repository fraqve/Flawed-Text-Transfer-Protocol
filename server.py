import socket
import fttp
import json

PORT = 8404
IP = "0.0.0.0"
try:
    with open("config.json") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Config file not found")
    exit(1)

ROOT_DIRECTORY = config["ROOT_DIRECTORY"]

def init_socket(ip_adr:str,port:int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip_adr,port))
    return sock

def accept_connexion(sock:socket.socket):
    sock.listen()
    user_sock,user_ip = sock.accept()
    return user_sock,user_ip

def format_data(data):
    return data.decode().strip()


if __name__ == "__main__":
    sock = init_socket(IP,PORT)
    while True:
        user_sock,user_ip = accept_connexion(sock)
        data = user_sock.recv(200).decode()
        method,code = fttp.validate_request(data)

        match method:
            case "GET":
                file_content,code,filename = fttp.handle_get_method(ROOT_DIRECTORY,data,user_sock)
                fttp.send_method(code,user_sock,ROOT_DIRECTORY,filename)
            case "UPLOAD":
                filepath = fttp.extract_filepath(data)
                data = b""
                while True:
                    chunk = user_sock.recv(200)
                    data += chunk
                    if b"\r\n\r\n" in data:
                        data = data.replace(b"\r\n\r\n",b"")
                        break 
                message,code = fttp.handle_upload_method(data,filepath,ROOT_DIRECTORY)
                fttp.send_method(code,user_sock,ROOT_DIRECTORY,filepath)
            case "ERROR":
                if code == 400:
                    fttp.send_method(400,user_sock,ROOT_DIRECTORY)

