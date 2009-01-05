# Pygame imports.
import pygame
from pygame.locals import *

# OpenGL imports.
from OpenGL.GL import *
from OpenGL.GLU import *

# Elasticity imports.
import net


# Connection parameters.
serverPort = 30000
clientPort = 30001
protocolId = "head"
deltaTime = 0.25
deltaTimeInMS = 250
timeOut = 10.0


def main():
    # Init connections.
    connection = net.Connection(protocolId, timeOut)    
    if not connection.start(clientPort):
        print "Could not start connection on port " + str(clientPort)
    connection.connect(("127.0.0.1", serverPort))
    connected = False
    
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
                del connection
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                del connection
                return
            if event.type == KEYUP and event.key == K_SPACE:
                data = "Client to server"
                connection.sendPacket(data, len(data))

        # Advance time.
        msPassed = clock.tick()
        secondsPassed = msPassed / 1000.0
        
        # Communicate with server
        if not connected and connection.isConnected():
            print "Client connected to server"
            connected = True
        if not connected and connection.connectFailed():
            print "Connection failed"
            del connection
            return
        #data = "Client to server"
        #connection.sendPacket(data, len(data))
        while True:
            dataReceived = connection.receivePacket(256)
            if not dataReceived:
                break
            print "Received packet from server"
        
        # Update the connection.
        connection.update(secondsPassed)

        # Render scene.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        
        # Finish rendering by showing the back buffer.
        pygame.display.flip()


if __name__ == '__main__':
    main()

