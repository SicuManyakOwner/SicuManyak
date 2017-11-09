import socket
from Classes import Answer

SERVER_IP = '127.0.0.1'
PORT = 7777
TYPE_LEN = 1


def send_request(request_type, dest_socket, data):
    if request_type == Answer.HND_TYPE:
        dest_socket.send(Answer.HND_TYPE + str(len(data)) + str(data))
    else:
        raise ValueError("Unknown request type", request_type)


def create_socket():
    """This functions purpose is to create a socket to get data from and perform a hand shake"""
    my_socket = socket.socket()
    my_socket.connect((SERVER_IP, PORT))
    if my_socket.recv(TYPE_LEN) == Answer.HND_TYPE:
        data_len = my_socket.recv(Answer.HND_LEN)
        data = my_socket.recv(int(data_len))
        if data == "handshake":
            send_request(Answer.HND_TYPE, my_socket, 'handshake')
        else:
            return None
    else:
        return None
    return my_socket


if __name__ == '__main__':
    print "Why is whould you run contact server?"
