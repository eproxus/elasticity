# System imports.
import socket

# Pygame imports.
import pygame
from pygame.locals import *

# OpenGL imports.
from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    # Server address and receive buffer size (auto sized for sending).
    host = "localhost"
    port = 50007
    address = (host,port)
    bufferSize = 1024
    
    # Create socket and bind it (bind is only needed for receiving data).
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.setblocking(False)
    try:
        clientSocket.bind(address)
    except:
        print "Could not bind socket. Error: " + socket.error
    
    # Init pygame.
    width = 800
    height = 600
    
    pygame.init()
    screen = pygame.display.set_mode((width, height), HWSURFACE | OPENGL | DOUBLEBUF)
    
    # Init OpenGL view.
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width)/height, .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Init OpenGL states.
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 0.0)

    # Init the clock.
    clock = pygame.time.Clock() 

    while True:
        # Get events.
        for event in pygame.event.get():
            if event.type == QUIT:
                clientSocket.close()
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                clientSocket.close()
                return
            if event.type == KEYUP and event.key == K_SPACE:
                try:
                    clientSocket.sendto('space', address)
                except:
                    print "Could not send data."

        # Advance time.
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.
        
        # Receive server data.
        try:
            data, addr = clientSocket.recvfrom(bufferSize)
            if data:
                print "Data received: " + data
        except:
            #print "No data received."
            pass

        # Render scene.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        
        
        # Finish rendering by showing the back buffer.
        pygame.display.flip()


if __name__ == '__main__':
    main()

