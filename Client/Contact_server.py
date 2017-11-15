import socket
from Classes import Answer

SERVER_IP = '127.0.0.1'
PORT = 7777
TYPE_LEN = 1


class Server:
    server_socket = None

    def __init__(self):
        """This functions purpose is to create a socket to get data from and perform a hand shake"""
        self.server_socket = socket.socket()
        self.server_socket.connect((SERVER_IP, PORT))
        if self.server_socket.recv(TYPE_LEN) == Answer.HND_TYPE:
            data = self.__get_data(Answer.HND_TYPE)
            if data == "handshake":
                self.__send_request(Answer.HND_TYPE, 'handshake')
            else:
                raise Exception("Error while attempting to connect")
        else:
            raise Exception("Server sent a non HANDSHAKE answer")

    def login(self, user_name):
        """
        This functions purpose is to get the status of the user from the server
        :param user_name: a string representing the name of the user
        :return: either welcome aboard meaning you are new or welcome back meaning you are known for the system
        """
        self.__send_request(Answer.LOG_TYPE, user_name)
        data = self.__get_data(self.server_socket.recv(TYPE_LEN))

        return data

    def get_user(self, user_name):
        """
        This functions purpose is to get the description of a certain user
        :param user_name: a string representing the name of the user
        :return: a tuple with all the data of the user in it
        """
        self.__send_request(Answer.ACC_TYPE, user_name)
        data = self.__get_data(self.server_socket.recv(TYPE_LEN))

        details = data.split('-')
        rating = details[0]
        likelihood = details[1]
        owns = details[2].split(',')
        awaiting_confirm = details[3].split(',')

        return rating, likelihood, owns, awaiting_confirm

    def __get_data(self, data_type):
        """
        This is an inner function which is supposed to get data by a specific request
        :param data_type: This is a char representing the type of the request
        :return: data from the request
        """
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

        data_len = int(self.server_socket.recv(data_len))
        data = self.server_socket.recv(data_len)
        return data

    def __send_request(self, request_type, data):
        """
        This functions purpose is to send a request for the server to get data back
        :param request_type: This is a char representing the type of the request
        :param data: extra parameters for the command
        :return: Nothing
        """
        if request_type == Answer.HND_TYPE:
            self.server_socket.send(Answer.HND_TYPE + str(len(data)) + str(data))

        elif request_type == Answer.LOG_TYPE:
            self.server_socket.send(Answer.LOG_TYPE + str(len(data)).zfill(Answer.LOG_LEN) + str(data))

        elif request_type == Answer.ACC_TYPE:
            self.server_socket.send(Answer.ACC_TYPE + str(len(data)).zfill(Answer.ACC_LEN) + str(data))

        else:
            raise ValueError("Unknown request type", request_type)


if __name__ == '__main__':
    print "Why would you run contact_server?"
    server = Server()
    print server.login("Elad")
    print server.get_user("Elad")


