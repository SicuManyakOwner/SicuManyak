import os

USER_PATH = "C:\\SicuManyak\\Users\\"
RATING_POS = 0
LIKELIHOOD_POS = 1
OWNS_POS = 2
AWAITING_POS = 3


class Answer:
    ___dest_sock = None
    ___answer_type = 'S'
    ___data_length = 0
    ___data = 0

    def __init__(self, dest_sock, answer_type, data_length, data):
        self.___dest_sock = dest_sock
        self.___answer_type = answer_type
        self.___data_length = data_length
        self.___data = data

    def get_dest_sock(self):
        return self.___dest_sock

    def get_answer_type(self):
        return self.___answer_type

    def get_data_length(self):
        return self.___data_length

    def get_data(self):
        return self.___data

    URL_TYPE = 'U'
    HND_TYPE = 'H'
    TRM_TYPE = 'T'
    PAY_TYPE = 'P'
    WRT_TYPE = 'W'
    SCM_TYPE = 'S'
    LOG_TYPE = 'L'
    ERR_TYPE = 'E'
    ACC_TYPE = 'A'

    LOG_LEN = 2
    HND_LEN = 1
    ERR_LEN = 2
    URL_LEN = 3
    TRM_LEN = 0
    PAY_LEN = 1
    SCM_LEN = 3
    ACC_LEN = 3


class User:

    ___user_name = "Hitler"
    ___owns = []
    ___awating_confirm = []
    ___rating = 0
    ___likelihood = 0

    def __init__(self, user_name):
        self.___user_name = user_name

    def new_user(self):
        self.___owns = []
        self.___awating_confirm = []
        self.___rating = 0
        self.___likelihood = 100

        with open(USER_PATH + self.___user_name + ".manyak", 'w') as user_file:
            user_file.write(str(self.___rating) + '-' + str(self.___likelihood) + '-' + ",".join(self.___owns) + '-' +
                            ",".join(self.___awating_confirm))

    def by_file(self):
        with open(USER_PATH + self.___user_name + ".manyak", 'r') as user_file:
            user_info = user_file.read().split('-')
            self.___rating = int(user_info[RATING_POS])
            self.___likelihood = int(user_info[LIKELIHOOD_POS])
            self.___owns = user_info[OWNS_POS].split(',')
            self.___awating_confirm = user_info[AWAITING_POS].split(',')

    def exists(self):
        return os.path.isfile(USER_PATH + self.___user_name + ".manyak")
