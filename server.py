import threading
import socket

host = "127.0.0.1" #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            messages = client.recv(1024)
            broadcast(messages)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nicknames} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(adress)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascci')
        nicknames.append(nickname)
        client.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joind the chat!' .encode('ascci'))
        client.send('Connectd To The Server!'.encode('ascci'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Serverd is Listening...")
receive()
