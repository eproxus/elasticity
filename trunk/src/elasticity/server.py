# Pygame imports.
import pygame
from pygame.locals import *

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
	if not connection.start(serverPort):
		print "Could not start connection on port " + str(serverPort)
	connection.listen()
	
	# Init the clock.
	clock = pygame.time.Clock()
	
	# Receive messages.
	while True:
		# Advance time.
		msPassed = clock.tick()
		secondsPassed = msPassed / 1000.0
		
		# Liste for data and bounce it.
		dataReceived = connection.receivePacket(256)
		if dataReceived:
			if connection.isConnected():
				data = "Bounce: " + dataReceived
				connection.sendPacket(data, len(data))
		
		# Send some more data.
		moreData = str(secondsPassed)
		connection.sendPacket(moreData, len(moreData))
		
		# Update the connection.
		connection.update(secondsPassed)
		
		pygame.time.wait(deltaTimeInMS)
	
	# Close the connection.
	del connection


if __name__ == '__main__':
	main()
