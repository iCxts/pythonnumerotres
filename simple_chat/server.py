import socket
from threading import Thread

HOST = '0.0.0.0'
PORT = 21001
s = None

connected_clients_number = 0
client_id_counter = 0
connected_client_ids = []
messages = []


def client_processor(conn, client_id):
    global connected_clients_number, messages, connected_client_ids

    while True:
        message_received = ""
        data = conn.recv(4096)
        if not data:
            print(f"Client {client_id} disconnected")
            connected_clients_number -= 1
            connected_client_ids.remove(client_id)
            break

        message_received += data.decode()

        print(f"Received message from client {client_id}: ", message_received)

        recipients = [cid for cid in connected_client_ids if cid != client_id]
        if recipients:
            messages.append({"from": client_id, "text": message_received, "need_to_send": recipients})

        undelivered = []
        for msg in messages:
            if client_id in msg["need_to_send"]:
                undelivered.append(f"From client {msg['from']}: {msg['text']}")
                msg["need_to_send"].remove(client_id)

        if undelivered:
            response = "\n".join(undelivered)
        else:
            response = "No new messages for you for now!"
        conn.send(response.encode())

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)

while True:
    conn, addr = s.accept()
    client_id_counter += 1
    connected_client_ids.append(client_id_counter)
    print(f"Client {client_id_counter} connected from address: ", addr)
    connected_clients_number += 1
    client_thread = Thread(target=client_processor, args=(conn, client_id_counter))
    client_thread.start()

s.close()
print("Server finished")

