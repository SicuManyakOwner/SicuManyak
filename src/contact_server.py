import socket

SERVER_IP = ''
SERVER_PORT = 0


def handle_request(request_index, client_socket, parameter=""):
    if request_index == 0 and parameter != "":
        client_socket.send('L' + len(parameter) + parameter)


def create_socket(request_index):
    client_socket = socket.socket()
    client_socket.connect((SERVER_IP, SERVER_PORT))
    handle_request(request_index, client_socket)