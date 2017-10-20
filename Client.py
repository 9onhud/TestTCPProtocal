import socket


def start_client():
    port = 5098

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((socket.gethostname(), port))

        # send name to server
        name = input("My name: ")
        client_socket.send(name.encode())

        status = client_socket.recv(1024).decode()
        if status == "ready":
            while True:
                data = input("Message :")
                if data in "Qq":
                    break

                client_socket.send(data.encode())
                print("Send :" + data)

                data_from_server = client_socket.recv(1024).decode()
                print("Receive :" + data_from_server)
    except Exception as e:
        print("You aren't connect.")
        print(e)
    finally:
        client_socket.close()
        print("Client is disconnect")


if __name__ == "__main__":
    start_client()
