import socket
from Classes import Answer

SERVER_IP = '127.0.0.1'
PORT = 7777
TYPE_LEN = 1


def login(server_socket, user_name):
    __send_request(Answer.LOG_TYPE, server_socket, user_name)
    data = __get_data(server_socket.recv(TYPE_LEN), server_socket)

    return data


def get_user(server_socket, user_name):
    __send_request(Answer.ACC_TYPE, server_socket, user_name)
    data = __get_data(server_socket.recv(TYPE_LEN), server_socket)

    details = data.split('-')
    rating = details[0]
    likelihood = details[1]
    owns = details[2].split(',')
    awaiting_confirm = details[3].split(',')

    return rating, likelihood, owns, awaiting_confirm


def __get_data(data_type, input_socket):

    if data_type == Answer.HND_TYPE:  # 1
        data_len = Answer.HND_LEN
    elif data_type == Answer.LOG_TYPE:  # 2
        data_len = Answer.LOG_LEN
    elif data_type == Answer.URL_TYPE:  # 3
        data_len = Answer.URL_LEN
    elif data_type == Answer.ERR_TYPE:  # 4
        data_len = Answer.ERR_LEN
    elif data_type == Answer.ACC_TYPE:  # 5
        data_len = Answer.ACC_LEN
    elif data_type == Answer.PAY_TYPE:  # 6
        data_len = Answer.PAY_LEN
    elif data_type == Answer.SCM_TYPE:  # 7
        data_len = Answer.SCM_LEN
    elif data_type == Answer.WRT_TYPE:  # 8
        data_len = Answer.WRT_LEN
    else:
        return None

    data_len = int(input_socket.recv(data_len))
    data = input_socket.recv(data_len)
    return data


def __send_request(request_type, dest_socket, data):
    if request_type == Answer.HND_TYPE:
        dest_socket.send(Answer.HND_TYPE + str(len(data)) + str(data))

    elif request_type == Answer.LOG_TYPE:
        dest_socket.send(Answer.LOG_TYPE + str(len(data)).zfill(2) + str(data))

    else:
        raise ValueError("Unknown request type", request_type)


def create_socket():
    """This functions purpose is to create a socket to get data from and perform a hand shake"""
    my_socket = socket.socket()
    my_socket.connect((SERVER_IP, PORT))
    if my_socket.recv(TYPE_LEN) == Answer.HND_TYPE:
        data = __get_data(Answer.HND_TYPE, my_socket)
        if data == "handshake":
            __send_request(Answer.HND_TYPE, my_socket, 'handshake')
        else:
            return None
    else:
        return None
    return my_socket


if __name__ == '__main__':
    print "Why would you run contact_server?"
    client_socket = create_socket()
    if client_socket is not None:
        answer = login(client_socket, "Ellad")
        if answer is not None:
            print answer
    else:
        print "cannot create connection"

