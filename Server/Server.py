import sys
import os
import socket
import select
from Classes import Answer, User

LOCAL_IP = '10.0.0.30'
USER_PATH = "C:\\SicuManyak\\Users\\"
ROOT_PATH = "C:\\SicuManyak\\"


answers_queue = []

inputs = []   # Sockets from which we expect input
outputs = []  # Sockets we want to write to


def initialize():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Setup a server socket

    server_port = raw_input("Enter the port to run the server on\n")  # Ask the admin for port
    while server_port.isdigit() is not True:
        server_port = raw_input("Enter the port to run the server on\n")

    server_socket.bind((LOCAL_IP, int(server_port)))  # Bind the server socket to this computer

    inputs.append(server_socket)

    if os.path.isdir(ROOT_PATH) is not True:  # Make a folder for the server, if it doesnt exist
        os.mkdir(ROOT_PATH)

    if os.path.isdir(USER_PATH) is not True:  # Make a folder for the users
        os.mkdir(USER_PATH)

    terminated = False
    while not terminated:

        readable_sockets, writable_sockets, error_sockets = select.select(inputs, outputs, [])  # check which of the
        handle_inputs(readable_sockets, server_socket)
        handle_messages(writable_sockets)
        # sockets we expect to use are actually free


def handle_messages(writable_sockets):
    """
    this function's purpose is to send answers to all available sockets
    :param writable_sockets: sockets which are available to write at
    :return:
    """
    for cur_socket in writable_sockets:
        for answer in answers_queue:
            if cur_socket == answer.get_dest_sock():
                cur_socket.send(answer.get_answer_type() + answer.get_data_length() + answer.get_data())
                answers_queue.remove(answer)
                outputs.remove(cur_socket)
                break


def handle_inputs(readable_sockets, server_socket):
    """
    This functions purpose is to read all inputs given by users, and create new requests accordingly

    :param readable_sockets: a list of sockets which are waiting to be read
    :param server_socket: the socket of the server
    """

    for cur_socket in readable_sockets:

        if cur_socket is server_socket:
            new_socket, new_ip = server_socket.accept(1)

            answers_queue.append(Answer(new_socket, Answer.HND_TYPE, 9, "handshake"))
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
                cur_socket.close()


def create_answer(client_socket, type):
    """
    This function's purpose is to read the data sent by the user, handle it, and then return an answer accordingly
    :param client_socket: a socket to read the data from and sent the data
    :param type: the type of the request
    :return:
    """

    if type == Answer.LOG_TYPE:
        data_len = client_socket.read(Answer.LOG_LEN)
    elif type == Answer.HND_TYPE:
        data_len = client_socket.read(Answer.HND_TYPE)

    if data_len.isdigit() is not True:
        send_error("ERR DATA LEN ISNT DIGIT")

    elif type == Answer.LOG_TYPE:
        username = client_socket.read(data_len)
        usr = User(username)
        if usr.exists():
            usr.by_file()
            log("User created : " + username + "\n")
            send_login_msg("Welcome aboard " + username, client_socket)
        else:
            usr.new_user()
            send_login_msg("Welcome back " + username, client_socket)

    elif type == Answer.HND_TYPE:
        data = client_socket.read(data_len)
        if data != "handshake":
            send_error("Hand shake error", client_socket)

    else:
        send_error("Unknown request", client_socket)


def send_login_msg(msg, dest_sock):
    answers_queue.append(Answer(dest_sock, Answer.ERR_TYPE, len(msg), msg))
    if dest_sock not in outputs:
        outputs.append(dest_sock)
    inputs.remove(dest_sock)


def send_error(error_msg, dest_sock):
    answers_queue.append(Answer(dest_sock, Answer.ERR_TYPE, len(error_msg), error_msg))
    if dest_sock not in outputs:
        outputs.append(dest_sock)
    inputs.remove(dest_sock)


def log(msg):
    """
    this function's purpose is to print a log message and write it to the log file
    :param msg: A log message
    :return:
    """
    print msg
    with open(ROOT_PATH + "log.log", 'a') as log_file:
        log_file.write(msg)


if __name__ == '__main__':
    #print "Remove the hashtag"
    initialize()
