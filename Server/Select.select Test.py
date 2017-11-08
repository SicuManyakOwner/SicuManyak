import socket
import select


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Setup a server socket

    server_socket.bind(('0.0.0.0', 7777))  # Bind the server socket to this computer
    server_socket.listen(1)
    inputs,outputs = [], []
    inputs.append(server_socket)
    readable_sockets, writable_sockets, error_sockets = select.select(inputs, outputs , [])

    for cur_socket in readable_sockets:

        if cur_socket is server_socket:
            new_socket, new_ip = server_socket.accept()

            new_socket.send("H" + str(19) + "handshake")


if __name__ == '__main__':
    main()