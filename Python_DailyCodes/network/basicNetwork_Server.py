import socket
import winsound

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF is address family, in this case IPV4. Sock_Stream specifices we're using ICP protocol

#binds the server to an IP Address and port number
server.bind(('0.0.0.0', 12345)) # ensures that the server will listen to any connection

# start listening for incoming connection
server.listen(1)
print('server is listening to client')

while True:
    # wait for client to connect 
    conn, addr = server.accept()
    print('connected to client at address: ', addr)

    while True:
        data = conn.recv(1024) # recieves data from client
        if not data: # if no data is recieved, client has disconnected
            break
            
        message = data.decode("utf-8") # converts data to an int 
        print(message)
        

    #close connection to client
    conn.close()
    print("disconnected")
    

