import socket
from threading import _start_new_thread


def start_server():
    def transferData(client):
        while True:
            data = client.recv(1024).decode()

            if not data:
                break

            print("Receive :" + data)

            data = data.upper()

            client.send(data.encode())
            print("Send :" + data)
        client.close()
        print("Client is disconnect")

    port = 5098
    player_number = 4

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), port))

    print("Server is wait for client's connect")
    server_socket.listen(player_number)  # wait for 4 player

    # Ver.1 >> If it have client's connect more than player_number, server_socket is close
    i = 1
    while i <= player_number:
        client, address = server_socket.accept()
        print("Number :" + str(i) + "Connect from :" + str(address))
        _start_new_thread(transferData, (client,))

        i += 1
    server_socket.close()
    print("Server is disconnect")

    # Ver.2 >> It can connect more than player_number
    i = 1
    while True :
        client, address = server_socket.accept()
        print("Number :" + str(i) + "Connect from :" + str(address))
        _start_new_thread(transferData, (client,))

        i += 1
    server_socket.close()
    print("Server is disconnect")


if __name__ == "__main__":
    start_server()
