# System imports.
import socket


class ConnectionMode:
	"""
	Some modes that the connection class can be in.
	"""
	uninitialized = 0
	client = 1
	server = 2


class ConnectionState:
	"""
	Some states that the connection class can have.
	"""
	disconnected = 0
	listening = 1
	connecting = 2
	connectFail = 3
	connected = 4


class Connection:
	def __init__(self, protocolId, timeout):
		self.__protocolId = protocolId
		self.__timeout = timeout
		self.__mode = ConnectionMode.uninitialized
		self.__running = False
		self.__clearData()
	
	def __del__(self):
		if self.isRunning():
			self.stop()
		
	def start(self, port):
		print "Start connection on port " + str(port)
		try:
			self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.__socket.bind(("", port))
			self.__socket.setblocking(False)
		except:
			return False
		self.__running = True
		self.onStart()
		return True
		
	def stop(self):
		print "Stop connection"
		connected = self.isConnected()
		self.__clearData()
		if self.__socket:
			self.__socket.close()
		self.__running = False
		if connected:
			self.onDisconnect()
		self.onStop()
		
	def isRunning(self):
		return self.__running
		
	def listen(self):
		print "Server listening for connections."
		connected = self.isConnected()
		self.__clearData()
		if connected:
			self.onDisconnect()
		self.__mode = ConnectionMode.server
		self.__state = ConnectionState.listening
		
	def connect(self, address):
		host, port = address
		print "Client connecting to " + str(host) + ":" + str(port)
		connected = self.isConnected()
		self.__clearData()
		if connected:
			self.onDisconnect()
		self.__mode = ConnectionMode.client
		self.__state = ConnectionState.connecting
		self.__address = address
		
	def isConnecting(self):
		return self.__state == ConnectionState.connecting
	
	def connectFailed(self):
		return self.__state == ConnectionState.connectFail
	
	def isConnected(self):
		return self.__state == ConnectionState.connected
	
	def isListening(self):
		return self.__state == ConnectionState.listening
	
	def getMode(self):
		return self.__mode
	
	def update(self, deltaTime):
		self.__timeoutAccumulator += deltaTime
		if self.__timeoutAccumulator > self.__timeout:
			if self.__state == ConnectionState.connecting:
				print "Connect timed out"
				self.__clearData()
				self.__state = ConnectionState.connectFail
				self.onDisconnect()
			elif self.__state == ConnectionState.connected:
				print "Connection timed out"
				self.__clearData()
				self.onDisconnect()
		
	def sendPacket(self, data, size):
		if not self.__address:
			return False
		packet = self.__protocolId + data
		try:
			sizeSent = self.__socket.sendto(packet, self.__address)
		except:
			sizeSent = 0
		return (size + len(self.__protocolId)) == sizeSent
		
	def receivePacket(self, size):
		try:
			packet, sender = self.__socket.recvfrom(size)
		except:
			return ""
		if packet[:len(self.__protocolId)] == self.__protocolId:
			if self.__mode == ConnectionMode.server and not self.isConnected():
				host, port = sender
				print "Server accepts connection from client " + str(host) + ":" + str(port)
				self.__state = ConnectionState.connected
				self.__address = sender
				self.onConnect()
			if sender == self.__address:
				if self.__mode == ConnectionMode.client and self.__state == ConnectionState.connecting:
					print "Client completes connection with server"
					self.__state = ConnectionState.connected
					self.onConnect()
				self.__timeoutAccumulator = 0.0
				return packet[len(self.__protocolId):]
				
		
	def getHeaderSize(self):
		return 4
	
	# Callback methods to implement in sub class.
	def onStart(self):
		print "onStart()"
		#pass
		
	def onStop(self):
		print "onStop()"
		#pass
		
	def onConnect(self):
		print "onConnect()"
		#pass
		
	def onDisconnect(self):
		print "onDisconnect()"
		#pass
	
	def __clearData(self):
		self.__state = ConnectionState.disconnected
		self.__timeoutAccumulator = 0.0
		self.__address = None
