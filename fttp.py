import socket
import os

def send_error_message(code:int,message:str,filepath:str,user_sock:socket.socket,root_directory):
    user_sock.sendall(f"FTTP SEND {filepath} {code} {message}".encode())
    user_sock.sendall("\r\n".encode())
    if os.path.exists(f"{root_directory}/{code}.html"):
        with open(f"{root_directory}/{code}.html","rb") as file:
            user_sock.sendall(file.read())
            user_sock.sendall("\r\n\r\n".encode())
    else:
        user_sock.sendall("<html></html>".encode())
        user_sock.sendall("\r\n\r\n".encode())


def extract_filepath(request:str):
    filepath = request.split()
    if len(filepath) >= 3:
        return filepath[2]
    else:
        return "ERROR"

def validate_request(request:str):
    request_keywords = request.split()
    match request_keywords:
        case ["FTTP","GET",*rest]:
            return "GET",200
        case ["FTTP","UPLOAD",*rest]:
            return "UPLOAD",200
        case _:
            return "ERROR",400

def send_method(code:int,user_sock:socket.socket,root_directory,filepath:str=""):
    if code == 200:
        user_sock.sendall(f"FTTP SEND {filepath} 200 OK".encode())
        user_sock.sendall("\r\n".encode())
    elif code == 404:
        send_error_message(404, "404 File not found", filepath, user_sock, root_directory)
    elif code == 400:
        send_error_message(400, "400 Trash request", filepath, user_sock, root_directory)
    elif code == 401:
        send_error_message(401, "401 path is a directory", filepath, user_sock, root_directory)
    elif code == 501:
        send_error_message(501, "501 Permission Error", filepath, user_sock, root_directory)
    elif code == 502:
        send_error_message(502, "502 OS error", filepath, user_sock, root_directory)
    elif code == 505:
        send_error_message(505, "505 unknown exception", filepath, user_sock, root_directory)
    
def upload_method(server_sock:socket.socket,filecontent,filepath:str):
    server_sock.sendall(f"FTTP UPLOAD {filepath}\r\n".encode())
    server_sock.sendall(filecontent)
    server_sock.sendall("\r\n\r\n".encode())
    
def handle_get_method(root_directory:str,request:str,user_sock:socket.socket):
    filepath = extract_filepath(request)
    fullpath = os.path.join(root_directory,filepath)
    if os.path.exists(fullpath):
        with open(fullpath,"rb") as file:
            user_sock.sendall(file.read())
            return "Sucess",200,filepath
    else:
        return "404 file not found".encode(),404,filepath
    
def handle_upload_method(filecontent,filepath,root_directory:str):
    fullpath = os.path.join(root_directory,filepath)
    try:
        os.makedirs(os.path.dirname(fullpath),exist_ok=True)
        with open(fullpath,"wb") as file:
            file.write(filecontent)
        return "Sucess",200
    except PermissionError:
        return "Permission Error",501
    except IsADirectoryError:
        return "path is a directory",401

    except OSError:
        return "OS error",502
    except Exception as e:
        return e,505
    




