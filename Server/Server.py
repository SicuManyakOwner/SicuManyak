import sys
import os
import socket
import select

LOCAL_IP = '0.0.0.0'

answers_queue = []

inputs = []   # Sockets from which we expect input
outputs = []  # Sockets we want to write to


def initialize():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Setup a server socket

    server_port = raw_input("Enter the port to run the server on\n")  # Ask the admin for port
    while server_port.isdigit() is not True:
        server_port = raw_input("Enter the port to run the server on\n")

    server_socket.bind('0.0.0.0', int(server_port))  # Bind the server socket to this computer

    inputs.append(server_socket)

    terminated = False
    while not terminated:

        readable_sockets, writable_sockets, error_sockets = select.select(inputs, outputs, [])  # check which of the
        # sockets we expect to use are actually free


def handle_inputs(readable_sockets, server_socket):
    """
    This functions purpose is to read all inputs given by users, and create new requests accordingly

    :param readable_sockets: a list of sockets which are waiting to be read
    :param server_socket: the socket of the server
    """

    for cur_socket in readable_sockets:

        if cur_socket is server_socket:
            new_socket, new_ip = server_socket.accept(1)

            answers_queue.append(Answer(new_socket, Answer.HND_TYPE, 5, "Peace"))
            if new_socket not in outputs:
                outputs.append(new_socket)

        else:
            rtype = cur_socket.read(1)

            if rtype is not None:
                create_answer(cur_socket, rtype)

                if new_socket not in outputs:
                    outputs.append(new_socket)

            else:
                inputs.remove(cur_socket)
                if cur_socket in outputs:
                    outputs.remove(cur_socket)


def create_answer(socket, type):
    NotImplementedError



if __name__ == '__main__':
    initialize()


class Answer:

    ___dest_sock = None
    ___answers_type = 'S'
    ___data_length = 0
    ___data = 0

    def __init__(self, dest_sock, answer_type, data_length, data):
        self.dest_sock = dest_sock
        self.answers_type = answer_type
        self.data_length = data_length
        self. data = data

    URL_TYPE = 'U'
    HND_TYPE = 'H'
    TRM_TYPE = 'T'
    PAY_TYPE = 'P'
    WRT_TYPE = 'W'
    SCM_TYPE = 'S'
