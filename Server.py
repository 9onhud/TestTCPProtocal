import socket
import threading


class MyThread(threading.Thread):
    def __init__(self, client_name, client, address):
        threading.Thread.__init__(self)
        self.name = client_name
        self.client = client
        self.address = address

    def run(self):
        print(self.name + " are Run")
        transferData(self.client)


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


def start_server():

    port = 5098
    player_number = 4

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), port))

    print("Server is wait for client's connect")
    server_socket.listen(player_number)  # wait for 4 player

    # wait 4 client(Player) connect and receive name from client
    client_threads = []
    for i in range(player_number):
        client, address = server_socket.accept()
        client_name = client.recv(1024).decode()  # wait to receive name from client

        thread = MyThread(client_name, client, address)
        client_threads.append(thread)
        print("Client:"+client_threads[i].name+" Connect")

    # run all thread(client)
    for thread in client_threads:
        thread.start()

    while True:
        if threading.active_count() == 1:
            server_socket.close()
            print("Server is disconnect")
            break


if __name__ == "__main__":
    start_server()
