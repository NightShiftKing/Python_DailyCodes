import socket

# set up client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.255', 12345))

while True:
    message = input("enter a message")
    if message.lower() == 'exit':
        break
    client.send(message.encode("utf-8"))

client.close()
