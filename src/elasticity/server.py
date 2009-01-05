# System imports.
import socket


def main():
    # Client address and receive buffer size (auto sized for sending).
    bufferSize = 1024
    
    # Create a server socket used for sending data.
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.setblocking(False)
    
    # Create one socket for each client and bind it to receive data.
    clientSocket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket1.setblocking(False)
    clientSocket1.bind(("localhost", 50008))
    
    # Add all clients to a list.
    clientSockets = [clientSocket1]
    
    # Receive messages.
    while True:
        data = ''
        address = ''
        
        # Try to receive from all clients.
        for clientSocket in clientSockets:
            try:
                data, address = clientSocket.recvfrom(bufferSize)
            except:
                #print "No data received."
                pass
        
        if data:
            print "Data received: " + data
            try:
                serverSocket.sendto(data, address)
                print "Data sent: " + data
            except:
                print "Could not send data."
    
    # Close client sockets.
    for clientSocket in clientSockets:
        clientSocket.close()
            
    # Close server sockets.
    serverSocket.close()


if __name__ == '__main__':
    main()
