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

    # wait 4 client(Player) connect and receive name from client
    def connect_client():
        threads = []
        for i in range(player_number):
            client, address = server_socket.accept()
            client_name = client.recv(1024).decode()  # wait to receive name from client

            threads.append(MyThread(client_name, client, address))
            print("Client: " + threads[i].name + " Connect")
        return threads

    # send to all client that all client are connection
    def send_ready():
        for thread in client_threads:
            thread.client.send("ready".encode())

    # run all thread(client)
    def start_threads():
        for thread in client_threads:
            thread.start()

    # if all client close connect, server close connect
    def check_connect_for_close():
        while True:
            if threading.active_count() == 1:
                server_socket.close()
                print("Server is disconnect")
                break

    port = 5098
    player_number = 4

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), port))

    print("Server is wait for client's connect")
    server_socket.listen(player_number)  # can connect 4 client

    client_threads = connect_client()   # wait to connect 4 clients
    send_ready()        # send ready to client
    start_threads()     # start game

    check_connect_for_close()


if __name__ == "__main__":
    start_server()
