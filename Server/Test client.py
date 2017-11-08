import socket


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(('127.0.0.1', 7777))
    data = my_socket.recv(1)
    if data == 'H':
        print my_socket.recv(int(my_socket.recv(2)))
    else:
        print "ERRRRRRRRRRRRRRRRR"


if __name__ == '__main__':
    main()